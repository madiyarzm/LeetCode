class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def helper(s, l, r):
            counter = 0
            
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1

            
            return counter
        
        res = 0
        for i in range(len(s)):
            res += helper(s, i, i)
            res += helper(s, i, i + 1)
        
        return res


