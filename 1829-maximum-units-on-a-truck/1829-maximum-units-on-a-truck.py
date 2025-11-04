import heapq
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        result = []

        result = [(-units, box) for box,units in boxTypes]
        heapq.heapify(result)

        ans = 0
        while truckSize > 0 and result:

            units, box = heapq.heappop(result)

            take = min(truckSize, box)

            ans += take * -units
            truckSize -= take
        
        return ans