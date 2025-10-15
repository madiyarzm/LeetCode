class Solution:
    def isValid(self, s: str) -> bool:
        
        b = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for bracket in s:

            #closing bracket
            if bracket not in b:
                stack.append(bracket)
            

            else:
                if not stack or b[bracket] != stack[-1]:
                    return False
                
                else:
                    stack.pop()

        if not stack:
            return True
        
        else:
            return False