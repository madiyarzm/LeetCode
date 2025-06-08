class Solution:
    def minOperations(self, nums: List[int]) -> int:          
        flips = 0
        i = 0
        
        while i <= len(nums) - 3:
            
            if nums[i] == 0:
                nums[i] = nums[i] ^ 1
                nums[i + 1] = nums[i + 1] ^ 1
                nums[i + 2] = nums[i + 2] ^ 1
                flips += 1
            
            i += 1
            
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return -1

        return flips