from collections import defaultdict

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1

            else:
                freq[num] = 1
        
        counter = nums.count(k)
        mx = counter

        for key in freq.keys():

            toy = nums.copy()

            if key == k:
                continue

            for i in range(len(toy)):

                if toy[i] == k:
                    toy[i] = -1
                
                elif toy[i] == key:
                    toy[i] = 1
                
                else:
                    toy[i] = 0
            
            current_sum = toy[0]
            max_sum = toy[0]

            for num in toy[1:]:
                current_sum = max(num, current_sum + num)
                max_sum = max(max_sum, current_sum)
            
            mx = max(mx,counter + max_sum)

        return mx


        