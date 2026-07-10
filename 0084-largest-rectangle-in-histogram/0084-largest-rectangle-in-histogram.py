class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        mx = 0

        heights.append(0) #to flush out stack at the end

        for i in range(len(heights)):

            start_index = i #by default left extending boundary is the current index

            while stack and stack[-1][1] > heights[i]: #if shorter bar appears (cant extend to the right)
                
                #pop it, capture the index and its height
                index, h = stack.pop()            
                mx = max(mx, (i - index) * h) #count the possible max region (left boundary - right_boundary * height)
                
                start_index = index #keep the last popped element, its gonna be next pushed elements left boundary
            
            stack.append((start_index, heights[i])) #push the left boundary and the height
        
        
        return mx
