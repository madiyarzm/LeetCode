class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        lower_bound = 0
        higher_bound = len(nums) - 1

        #1 + 3 // 2 = 2
        while lower_bound <= higher_bound:
            
            mid = (higher_bound + lower_bound) // 2

            if nums[mid] == target:
                return mid
            
            # 5 > 3
            elif target > nums[mid]:
                lower_bound = mid + 1
            
            elif target < nums[mid]:
                higher_bound = mid - 1
            
        
        return lower_bound