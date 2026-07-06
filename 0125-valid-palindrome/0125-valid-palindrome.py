class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1
        s_l = s.lower()

        while l <= r:
            if (s_l[l].isalnum() and s_l[r].isalnum()) and s_l[l] != s_l[r]:
                return False
            
            elif (s_l[l].isalnum() and s_l[r].isalnum()) and s_l[l] == s_l[r]:
                l += 1
                r -= 1
                continue
            
            elif not s_l[l].isalnum():
                while  l <= r and not s_l[l].isalnum() :
                    l += 1
                    
            elif not s_l[r].isalnum():
                while l <= r and not s_l[r].isalnum():
                    r -= 1
                
        return True
            
