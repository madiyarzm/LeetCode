class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water = 0

        while l < r:
            
            #move the shorter max border
            if l_max < r_max:
                l += 1

                l_max = max(l_max, height[l]) #update if taller found
                water += l_max - height[l] #for this invidiual block, smallest of borders - current height
            
            else:
                r -= 1

                r_max = max(r_max, height[r])
                water += r_max - height[r]
        
        return water

