import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #we have specific range of min and max 
        left, right = 1, max(piles)
        best = max(piles)

        #finds the time spent to eat all piles, uses ceiling division
        def helper(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)
            
            return time

        #binary search for best rate
        while left <= right:

            mid = (left + right) // 2
            current_rate = helper(mid)

            #target rate smaller, more left
            if current_rate <= h:
                best = mid
                right = mid - 1

            else:
                left = mid + 1
        
        return best