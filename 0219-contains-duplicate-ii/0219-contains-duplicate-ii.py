class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mapping = {}

        for i in range(len(nums)):
            
            if nums[i] in mapping:
                if abs(mapping[nums[i]] - i) <= k:
                    return True

            mapping[nums[i]] = i
        
        return False
