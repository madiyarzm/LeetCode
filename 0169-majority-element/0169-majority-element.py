class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums[:] = sorted(nums)
        counter = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                counter = counter + 1

            else:
                counter = 1

            if counter > len(nums) // 2:
                return nums[i]   

        return nums[0]   