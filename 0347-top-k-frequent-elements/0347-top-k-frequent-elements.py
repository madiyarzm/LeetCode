from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        #now we have 1 -> 3, 2 -> 2, 3 -> 1

        result = []
        mx_list = list(freq.values())

        while k > 0:
            mx = max(mx_list)
            for number, count in freq.items():
                if mx == count:
                    result.append(number)
                    freq.pop(number)
                    break
            
            mx_list.remove(mx)
            k -= 1

        return result