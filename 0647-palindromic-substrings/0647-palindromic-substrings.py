class Solution:
    def countSubstrings(self, s: str) -> int:
        

        #helper function, goes outwards and checks whether palindromeness is saved
        def count_palindrome(s, l, r):
            counter = 0
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                counter += 1
                l -= 1
                r += 1
            
            return counter


        #account for odd length, and even length palindromes
        result = 0
        for i in range(len(s)):
            result += count_palindrome(s, i, i)
            result += count_palindrome(s, i, i + 1)
            

        return result

#abcabac