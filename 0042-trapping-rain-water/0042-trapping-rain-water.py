class Solution:
    def trap(self, height: List[int]) -> int:
        i = 1
        j = len(height) - 2
    
        water = 0
        left_mx = height[0]
        right_mx = height[-1]
        
        while i <= j:
            if left_mx <= right_mx:
                left_mx = max(left_mx, height[i])
                water = water + max(0, left_mx - height[i])
                
                i += 1
            
            else:
                right_mx = max(right_mx, height[j])
                water = water + max(0, right_mx - height[j])
                
                j -= 1
        
        return water
