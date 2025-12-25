import heapq
class MedianFinder:

    def __init__(self):

        #set up 2 empty lists for an object
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        

        #empty or if it belongs to lower half
        if len(self.maxheap) == 0 or num <= self.maxheap[0] * -1:
            heapq.heappush(self.maxheap, num * -1)
        
        else:
            heapq.heappush(self.minheap, num)
        
        if len(self.maxheap) >= len(self.minheap) + 2:
            heapq.heappush(self.minheap, self.maxheap[0] * -1)
            heapq.heappop(self.maxheap)
        
        elif len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, self.minheap[0] * -1)
            heapq.heappop(self.minheap)
            

    def findMedian(self) -> float:
        if (len(self.maxheap) + len(self.minheap)) % 2 == 0:
            return (self.maxheap[0] * -1 + self.minheap[0]) / 2
        
        else:
            return self.maxheap[0] * -1


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()