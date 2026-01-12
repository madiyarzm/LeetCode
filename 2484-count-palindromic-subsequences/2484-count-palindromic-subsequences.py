class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        
        def findPrefix(s):
            cntArr = [0]*10
            dp = [[[0]*10 for _ in range(10)] for _ in range(n)]
            for i in range(n) :
                num = int(s[i])
                if i-1 >= 0 :
                    for x in range(10):
                        for y in range(10):
                            dp[i][x][y] = dp[i-1][x][y]
                            # if curr num is y then we get new xy combo
                            if y == num : 
                                dp[i][x][y] += cntArr[x]
                cntArr[num] += 1
            return dp
        
        pre = findPrefix(s)
        suff = findPrefix(s[::-1])[::-1]   
        # suff[i][x][y] is actually suff[i][y][x] here because of reverse string prefix finding
        
        res = 0
        for i in range(2,n-2):
            for x in range(10):
                for y in range(10):
                    res = (res + pre[i-1][x][y] * suff[i+1][x][y]) % mod
        return res