class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        #first we need to precompute last occurence of each character

        last = {}
        for i, letter in enumerate(s):
            last[letter] = i
        
        result = []
        counter = 0
        mx = 0

        for i in range(len(s)):
            mx = max(mx, last[s[i]])
            counter += 1

            if i == mx:
                result.append(counter)
                counter = 0



        return result
            

