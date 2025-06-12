class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        mx_difference = abs(nums[-1] - nums[0])

        for i in range(len(nums) - 1):
            mx_difference = max(mx_difference, abs(nums[i] - nums[i + 1]))
        
        return mx_difference
