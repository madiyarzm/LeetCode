import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        
        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1

            else:
                freq[word] = 1
        
        lst = []
        for key, value in freq.items():
            heapq.heappush(lst, (-value, key))
        
        result = []
        for i in range(k):
            k, v = heapq.heappop(lst)
            result.append(v)
    
        return result