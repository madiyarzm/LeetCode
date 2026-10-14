import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        
        freq = {}

        #prepare hashmap with frequencies for each word
        for word in words:
            if word in freq:
                freq[word] += 1

            else:
                freq[word] = 1
        
        lst = []
        for key, value in freq.items():
            lst.append((-value, key))
        
        #building list, and heapifying it once is O(N) vs one by one push O(NlogN)
        heapq.heapify(lst)
        
        #pop needed amount, unpack the tuple and append values only
        result = []
        for _ in range(k):
            key, v = heapq.heappop(lst)
            result.append(v)
    
        return result