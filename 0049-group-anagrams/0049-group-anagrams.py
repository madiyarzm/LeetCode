from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = defaultdict(list)

        for word in strs:
            
            freq = [0] * 26

            for letter in word:
                freq[ord(letter) - ord('a')] += 1
        
            hmap[tuple(freq)].append(word)
            
        result = []
        for group in hmap.values():
            result.append(group)
        
        return result

