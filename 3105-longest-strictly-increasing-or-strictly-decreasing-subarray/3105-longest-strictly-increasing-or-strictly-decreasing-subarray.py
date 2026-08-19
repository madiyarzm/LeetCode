class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        mx = 1
        current = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                current += 1
            
            else:
                current = 1

            mx = max(mx, current)
                
        
        mn = 1
        current = 1

        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                current += 1
            
            else:
                current = 1
        
            mn = max(mn, current)

        print(mx)
        print(mn)      
        

        return max(mx, mn)

