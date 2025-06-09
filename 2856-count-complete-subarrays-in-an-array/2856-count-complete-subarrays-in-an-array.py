class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        k = len(set(nums))
        
        l = 0
        r = 1
        seen = {}
        
        unique = 0
        count = 0
        
        for r in range(len(nums)):
            
            if nums[r] not in seen:
                seen[nums[r]] = 0

            seen[nums[r]] += 1
            if seen[nums[r]] == 1:
                unique += 1
            
            
            while unique == k:
                
                #if until r there are all unique numbers
                #adding one more will not make it invalid
                count += len(nums) - r
                
                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    unique -= 1
                
                
                l += 1
            
        
        return count