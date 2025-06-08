class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                j = 0
                while j < 3:
                    if nums[i + j] == 0:
                        nums[i + j] = 1
                    else:
                        nums[i + j] = 0  
                    j += 1
                flips += 1

        for i in range(len(nums)):
            if nums[i] == 0:
                return -1

        return flips