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

        #while heap is not empty
        while heap:

            #get first most common element
            count1, char1 = heapq.heappop(heap)
            
            #if its empty already, and there is more than 1 element, then its impossible
            if not heap:
                if count1 < -1:
                    return ""
                
                result.append(char1)
                break

            #get second most common element
            count2, char2 = heapq.heappop(heap)

            #add these elements
            result.append(char1)
            result.append(char2)

            #reduce their counts
            count1 += 1
            count2 += 1


            #if there are still some counts left, put tuple back into heap
            if count1 < 0: 
                heapq.heappush(heap, (count1, char1))

            if count2 < 0: 
                heapq.heappush(heap, (count2, char2))

        return "".join(result)
        


        