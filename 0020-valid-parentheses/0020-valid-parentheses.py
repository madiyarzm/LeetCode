class Solution:
    def isValid(self, s: str) -> bool:
        
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for bracket in s:

            if bracket not in close_to_open:
                stack.append(bracket)

            else:
                if not stack or close_to_open[bracket] != stack[-1]:
                    return False
                
                stack.pop()
        
        return not stack