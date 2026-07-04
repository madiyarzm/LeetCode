class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)
        max_streak = 0

        for number in numSet:
            
            #if there is no previous number in list, start streak counting
            if number - 1 not in numSet:
                current_num = number
                current_streak = 1

                while (current_num + 1) in numSet: #until streak is increasing
                    current_num += 1
                    current_streak += 1
            
                max_streak = max(max_streak, current_streak)
        
        return max_streak