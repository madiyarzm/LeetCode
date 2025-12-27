from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()
        l = r = 0
        result = []

        #right pointer inbounds
        while r < len(nums):
            
            #pop from right, while its non-empty and until its not monotonically decreasing
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            #when its monotically decreasing add
            q.append(r)

            #check whether current leftmost(max) is inbounds, if not remove from left
            if l > q[0]:
                q.popleft()

            #at least k sized window, and then start appending, once reached start l+=1
            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1
            
            r += 1

        return result

