#This is greedy problem, since we dont have to work through all possible paths
#We can end early, with found solution
#It's also reaching the end problem, so most likely greedy problem

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reach = 0
        for i in range(len(nums)):
            
            if i > max_reach: #if max reach is beyond current index, we cant reach last
               return False #so we will end here
            
            max_reach = max(max_reach, i + nums[i]) #update if curr maxreach is smaller
    
            if max_reach >= len(nums) - 1:
                return True
            
        return False