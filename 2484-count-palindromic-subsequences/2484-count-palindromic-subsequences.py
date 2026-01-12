class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)

        def findPrefix(s):

            #how many digits we meet accessed by the value of digit
            cnt_digits = [0] * 10

            #3D DP, stores value of possible pairs, at i,j coordinate for given index
            dp = [[[0] * 10 for _ in range(10)] for _ in range(n)]

            for i in range(n):
                num = int(s[i])
                if i - 1 >= 0:
                    for x in range(10):
                        for y in range(10):

                            #copy forward from previous indexs result
                            dp[i][x][y] = dp[i - 1][x][y]

                            # if we met, Y from XY pair
                            if y == num:

                                #add counts of X, since its same as count(X) = count(XY)
                                dp[i][x][y] += cnt_digits[x]
                
                cnt_digits[num] += 1

            return dp
        
        prefix = findPrefix(s)
        suffix = findPrefix(s[::-1])[::-1]

        result = 0
        for i in range(2, n - 2):
            for x in range(10):
                for y in range(10):

                    #combinatorically find all possible consequences
                    #valid pairs up to i, valids pairs after i
                    result = (result + prefix[i - 1][x][y] * suffix[i + 1][x][y]) % mod
        
        return result