from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        #create empty buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        #reverse num,count -> count, num
        for num, count in freq.items():
            buckets[count].append(num)

        #use buckets, so we dont have to sort through
        res = []

        #one bucket can have multiple numbers
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
         
            
          