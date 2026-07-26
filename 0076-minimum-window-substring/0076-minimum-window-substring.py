from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #frequency mapping of both strings
        freq_t = defaultdict(int)
        for char in t:
            freq_t[char] += 1
        
        l = 0
        freq = defaultdict(int)
        have = 0
        need = len(freq_t)
        
        #we need substring itself, and result lenght used as check for it to be found or not found
        result = [-1, -1]
        result_len = float('inf')

        for r in range(len(s)):
            letter = s[r]
            freq[s[r]] += 1   #expand the window, and update frequency map

            if letter in freq_t and freq[letter] == freq_t[letter]:    #if we get needed frequency for some letter, add to [have]
                have += 1

            while have == need: #until we have valid window, we ll try to optimize it, by shrinking and keeping validity

                if (r - l + 1) < result_len:    #update to minimum size and bounds
                    result_len = r - l + 1
                    result = [l, r]

                freq[s[l]] -= 1 #remove freq, shrink from left

                if s[l] in freq_t and freq[s[l]] < freq_t[s[l]]:   #if shrinking distorts the balance, we are lacking needed letter 
                    have -= 1 

                l += 1


        l, r = result
        if result_len != float('inf'):
            return s[l:r+1]
        
        return ""
                