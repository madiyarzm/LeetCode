import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        
        freq = {}

        for word in words:
            if word in freq:
                freq[word] += 1
            
            else:
                freq[word] = 1
        
        sorted_freq = dict(sorted(freq.items(), key = lambda item: (-item[1], item[0])))

        result = []
        counter = 0

        for key in sorted_freq.keys():
            if counter == k:
                break

            result.append(key)
            counter += 1
        
        return result