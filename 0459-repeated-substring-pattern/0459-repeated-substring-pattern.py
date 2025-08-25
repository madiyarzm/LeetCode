class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        #we double it, remove first and last characters, 
        #and check whether s is in 2*s, if its, its True, since string rotation comes back
        #to original string, and can wrap each other

        double = s + s

        return s in double[1:-1]