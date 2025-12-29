class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mx = 0
        zeroes = 0

        l = r = 0
        for r in range(len(nums)):

            if nums[r] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                
                l += 1
            
            mx = max(mx, r - l + 1)

        return mx
