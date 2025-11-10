class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        resLen = 0

        for i in range(len(s)):
            
            #we expand from the center
            l , r = i, i

            #until we are in boundaries, and expansion is working
            while l >= 0 and r < len(s) and s[l] == s[r]:

                #if current length is longer than updated mx len
                if (r - l + 1) > resLen:

                    #slice needed substring, [)
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                l -= 1
                r += 1

            #for even length, 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1

                l -= 1
                r += 1
            
        return res
            