class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        last1 = word1[-1]
        last2 = word2[-1]

        # use list() instead of split() to break into characters
        l1 = list(word1) + len(word1) * [" "]
        l2 = list(word2) + len(word2) * [" "]

        i = 0
        while i < len(l1) and l1[i] != last1:
            l1.append(" ")
            i += 2

        j = 1
        l2[0] = " "
        while j < len(l2) and l2[j] != last2:
            l2.append(" ")
            j += 2

        # merge alternately, but check bounds
        merged = []
        max_len = max(len(word1), len(word2))
        for k in range(max_len):
            if k < len(word1):
                merged.append(word1[k])
            if k < len(word2):
                merged.append(word2[k])

        return "".join(merged)
