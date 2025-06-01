class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        water = 0
        mx_water = float('-inf')

        while i < j:
            water = min(height[i], height[j]) * (j - i)

            if mx_water < water:
                mx_water = water

            if min(height[i], height[j]) == height[i]:
                i += 1
            
            else:
                j -= 1

        return mx_water