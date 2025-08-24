class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        #we just check whether there are 999, and then 888 until 000

        n = 9

        while n >= 0:
            if str(n) * 3 in num:
                return str(n) * 3
            
            n -= 1
        
        return ""