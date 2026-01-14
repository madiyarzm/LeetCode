import heapq
class MedianFinder:

    def __init__(self):
        #1. maxheap -> array
        self.maxheap = [] # M: O(n / 2)
        
        #2. minheap -> array
        self.minheap = [] # M: O(n / 2)

    def addNum(self, num: int) -> None:
        #maxheap is empty, incoming number is lower than maxheap root
            #maxheap.add(num)
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, num * -1) # T: O(log2n)
        
        #else (incoming number is higher than maxheap root) -> 
            #belongs to minheap
        else:
            heapq.heappush(self.minheap, num)   # T: O(log2n)
        
        #maxheap > minheap + 1
            #pop the root of maxheap -> minheap (heapifyng)
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap)) # T: O(log2n)
        
        #minheap > maxheap 
            #pop the root of minheap -> maxheap (heapifying)
        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap)) # T: O(log2n)


    def findMedian(self) -> float: #T: O(1)
        
        #if length of the maxheap > minheap (+1)
            #pop maxheaps root, return 
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0] * -1
        
        #length are equal, 
            #pop minheap roots, and maxheaps root, add them and divide by 2. (float)
        else:
            return (self.maxheap[0] * -1 + self.minheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()