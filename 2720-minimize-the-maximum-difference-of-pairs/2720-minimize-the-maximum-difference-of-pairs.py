class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # use this pair and skip both
                else:
                    i += 1  # skip to try next pair
            return count >= p

        left, right = 0, nums[-1] - nums[0]
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                answer = mid
                right = mid - 1  # try to find smaller max diff
            else:
                left = mid + 1  # increase allowed diff

        return answer
