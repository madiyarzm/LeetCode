class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        mx = 0
        current = 1

        l = 0
        r = len(heights) - 1 

        while l < r:
            current = min(heights[l], heights[r]) #choose the shorter bar out of 2 borders
            mx = max(mx, current * (r - l)) #update our max trapped water

            if current == heights[l]: #if our left border is smaller, then move it
                l += 1

            else: 
                r -= 1
        
        return mx