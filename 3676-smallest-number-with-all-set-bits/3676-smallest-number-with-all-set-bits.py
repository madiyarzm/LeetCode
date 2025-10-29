class Solution:
    def smallestNumber(self, n: int) -> int:
        
        i = 1
        while i <= n:
            i = i * 2
        
        return i - 1