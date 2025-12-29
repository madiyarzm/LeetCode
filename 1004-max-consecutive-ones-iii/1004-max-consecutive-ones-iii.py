class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mx = 0
        zeroes = 0

        #we set up 2 pointers
        l = r = 0
        for r in range(len(nums)):
            
            if nums[r] == 0:
                zeroes += 1

            #shrink window, until zeroes are in allowed number
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                
                #shrink left border
                l += 1
            
            #update the maximum
            mx = max(mx, r - l + 1)
        
        return mx
