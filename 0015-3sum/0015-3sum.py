class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # x + y + z = 0
        # -x = y + z
        # -x -> target, standard Two sum, y + z = target
        # avoid duplicates outer and inner loop, neigbhor matches

        result = []
        nums.sort() #sort to use Two pointers sum later

        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i - 1]: #outer loop duplicate prevention
                continue

            l = i + 1
            r = len(nums) - 1
            target = -1 * nums[i] 
            
            while l < r:

                if l < r and nums[l] + nums[r] < target:
                    l += 1
                
                elif l < r and nums[l] + nums[r] > target:
                    r -= 1
                
                if l < r and nums[l] + nums[r] == target:
                    result.append([target * -1, nums[l], nums[r]])
                    l += 1
                    r -= 1 

                    while l < r and nums[l] == nums[l - 1]: #left pointer can be same element too
                        l += 1
        


        return result