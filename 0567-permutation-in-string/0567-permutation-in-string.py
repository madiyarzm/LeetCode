from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #create dictionary to check the frequency of letters
        freq = defaultdict(int)
        l = 0

        for char in s1:
            freq[char] += 1

        freq2 = defaultdict(int)

        for r in range(len(s2)):

            freq2[s2[r]] += 1

            while (r - l + 1) > len(s1): #shrink the window, if its invalid (in this case size)
                freq2[s2[l]] -= 1

                if freq2[s2[l]] == 0:  #dont forget to delete counter, if no frequency left
                    del freq2[s2[l]] 

                l += 1
            
            if freq == freq2: #compare both of them
                return True
            
        
        return False
