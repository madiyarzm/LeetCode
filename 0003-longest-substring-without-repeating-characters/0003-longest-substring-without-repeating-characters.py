class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()

        l = 0
        r = 0
        mx_l = 0

        for r in range(len(s)):

            while s[r] in my_set:
                my_set.remove(s[l])

                l += 1
            
            my_set.add(s[r])
            mx_l = max(mx_l, r - l + 1)
            
        return mx_l

