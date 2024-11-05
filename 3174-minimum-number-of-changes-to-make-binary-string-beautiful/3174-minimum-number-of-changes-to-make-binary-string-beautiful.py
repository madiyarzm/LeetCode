class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0

        for i in range(1, len(s), 2):
            if s[i - 1] != s[i]:
                changes = changes + 1

        #"11 000 111"  

        return changes
        

               