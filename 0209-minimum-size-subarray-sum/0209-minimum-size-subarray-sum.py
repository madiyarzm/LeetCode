class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        mn_l = float('inf')

        current_sm = 0


        for r in range(len(nums)):
            current_sm = current_sm + nums[r]

            while current_sm >= target:
                mn_l = min(mn_l, r - l + 1)
                current_sm = current_sm - nums[l]
                l += 1
        
        if mn_l == float('inf'):
            return 0

        return mn_l