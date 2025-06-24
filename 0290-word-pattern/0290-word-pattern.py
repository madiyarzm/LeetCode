class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        

        mapping = {}
        unique_words = set()
        lst = s.split(" ")

        if len(pattern) != len(lst):
            return False


        for i in range(len(lst)):

            if pattern[i] in mapping:
                if mapping[pattern[i]] != lst[i]:
                    return False

            else:  
                if lst[i] in unique_words:
                    return False

                mapping[pattern[i]] = lst[i]
                unique_words.add(lst[i])
        
        return True
