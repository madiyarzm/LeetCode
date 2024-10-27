class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums[:] = sorted(nums)
        return nums[len(nums) // 2]