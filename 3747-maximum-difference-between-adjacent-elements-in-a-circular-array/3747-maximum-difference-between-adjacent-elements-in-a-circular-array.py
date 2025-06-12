class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        mx_difference = float('-inf')

        i = 1
        while i < len(nums):
            mx_difference = max(mx_difference, abs(nums[i] - nums[i - 1]))
            i += 1
        
        return max(mx_difference, abs(nums[-1] - nums[0]))