import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq = {}

        #building frequency dictionary
        for letter in s:

            if letter in freq:
                freq[letter] += 1

            else:
                freq[letter] = 1

        #list comprehension to create list out of tuple pairs of count and letters
        heap = [(-count, char) for char, count in freq.items()]
        
        heapq.heapify(heap)

        result = []

        while heap:
            count1, char1 = heapq.heappop(heap)
            
            if not heap:
                if count1 < -1:
                    return ""
                
                result.append(char1)
                break

            count2, char2 = heapq.heappop(heap)

            result.append(char1)
            result.append(char2)

            count1 += 1
            count2 += 1

            if count1 < 0: 
                heapq.heappush(heap, (count1, char1))

            if count2 < 0: 
                heapq.heappush(heap, (count2, char2))

        return "".join(result)
        


        