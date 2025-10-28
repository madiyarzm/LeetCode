class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        zeroes_ind = []

        for i in range (len(nums)):
            if nums[i] == 0:
                zeroes_ind.append(i)
            
        counter = 0

        for start in zeroes_ind:
            for turn in [1, -1]:
                lst = nums.copy()
                curr = start + turn
                direction = turn
                zeroes = set()

                while 0 <= curr < len(lst):

                    if lst[curr] == 0:
                        curr += direction
                        
                    
                    else:
                        lst[curr] -= 1
                        direction = direction * (-1)
                        curr += direction
                
                if all(x == 0 for x in lst):
                    counter += 1
        
        return counter