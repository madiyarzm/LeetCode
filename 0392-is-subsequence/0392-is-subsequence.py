class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) == 0 and len(s) != 0:
            return False

        if len(t) == len(s):
            if s == t:
                return True
            else:
                return False

        i = 0
        j = 0

        while i < len(s):
            while j < len(t) and s[i] != t[j]:
                j += 1
                #print("here are pairs ", s[i], t[j])

            if j == len(t):
                return False

            i += 1
            j += 1

        return True