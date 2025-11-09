class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #unique = set(nums)
        counter = nums.count(k)
        mx = counter

        for key in range(1,51):
            if key == k:
                continue

            current_sum = max_sum = 0

            for num in nums:
                if num == key:
                    current_sum += 1
                elif num == k:
                    current_sum -= 1

                current_sum = max(current_sum, 0)
                max_sum = max(max_sum, current_sum)

            mx = max(mx, counter + max_sum)

        return mx
