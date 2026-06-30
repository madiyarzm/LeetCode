class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):

            #check whether we have complement stored in dict
            if target - nums[i] in hmap:
                return [hmap[target - nums[i]], i]
            
            #if not store the index, for future
            hmap[nums[i]] = i