class Solution:
    def countSubstrings(self, s: str) -> int:
        
        counter = 0

        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1

        return counter

#abcabac