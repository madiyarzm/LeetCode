import heapq
#from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []

        l = 0
        #active = defaultdict(bool)

        for r in range(len(nums)):
            heapq.heappush(heap, (nums[r] * -1, r)) #push tuple containing number and its index in the list
            #active[r] = True
             
            if (r - l + 1) > k: #1 step at a time, so use if to shrink
                #active[l] = False
                l += 1

            while heap:

                item, item_id = heap[0]

                if item_id < l:    #if top of the heap is out of window, pop it
                    heapq.heappop(heap)
                    continue
                
                else:
                    if (r - l + 1) == k: #when we form window, read and return the maximum
                        result.append(item * -1)

                    break


        return result