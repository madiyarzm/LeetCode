class Solution:
    def jump(self, nums: List[int]) -> int:
        
        max_reach = 0
        current_end = 0
        counter = 0
        for i in range(0, len(nums) - 1):

            max_reach = max(max_reach, i + nums[i])

            if max_reach >= len(nums) - 1:
                return counter + 1

            if current_end == i:
                counter = counter + 1
                current_end = max_reach

        return counter