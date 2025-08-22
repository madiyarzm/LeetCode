class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()

        l2w = {}
        w2l = {}

        if len(pattern) != len(words):
            return False

        for letter, word in zip(pattern, words):

            if letter in l2w and word != l2w[letter]:
                return False

            if word in w2l and letter != w2l[word]:
                return False

            l2w[letter] = word
            w2l[word] = letter
        
        return True