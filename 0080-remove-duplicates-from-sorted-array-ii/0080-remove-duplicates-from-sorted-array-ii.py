class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        #if not nums:
            #return 0

        j = 0
        counter = 0
        for i in range(len(nums)):
            
            if nums[i] == nums[i - 1]:
                counter = counter + 1
            
            else:
                counter = 1
            
            if counter <= 2:
                nums[j] = nums[i]
                j = j + 1
        
        nums[:] = nums[:j]

        return len(nums)
