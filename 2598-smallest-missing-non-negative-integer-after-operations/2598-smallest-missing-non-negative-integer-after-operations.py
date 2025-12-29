class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        mod = {}

        for number in nums:

            remainder = number % value

            if remainder in mod:
                mod[remainder] += 1
            
            else:
                mod[remainder] = 1
        
        i = 0
        while True:

            r = i % value

            if mod.get(r, 0) == 0:
                return i

            mod[r] -= 1

            i += 1
        
        return i
