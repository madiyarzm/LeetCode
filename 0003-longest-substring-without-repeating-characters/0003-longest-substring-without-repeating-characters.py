class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        mx = 0
        window_set = set() #to check for duplicates in O(1)

        for r in range(len(s)):

            while s[r] in window_set: #slide window, if current element is not unique
                window_set.remove(s[l])  #shift boundary from left
                l += 1
            
            window_set.add(s[r])

            mx = max(mx, r - l + 1)

        
        return mx
