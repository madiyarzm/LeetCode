class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        hills = 0 
        valleys = 0

        clean = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                clean.append(nums[i])
        
        for i in range(1, len(clean) - 1):
            if clean[i - 1] < clean[i] and clean[i] > clean[i + 1]:
                #print(clean[i])
                hills += 1
            
            elif clean[i - 1] > clean[i] and clean[i] < clean[i + 1]:
                #print(clean[i])
                valleys += 1
        
        return hills + valleys