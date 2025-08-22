class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        #edge case
        if len(name) > len(typed):
            return False

        i = 0
        j = 0

        while j < len(typed):

            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            
            #if its same 2 keys then check next character (until no unique)
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            
            #if mismatch then false
            else:
                return False
        
        #i should reach the end of name length, otherwise its wrong
        if i == len(name):
            return True
        
        return False