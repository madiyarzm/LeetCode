class Solution:
    def isValid(self, s: str) -> bool:
        

        #key closing, value opening
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []

        for bracket in s:
            
            #if its opening, add to stack
            if bracket not in close_to_open:
                stack.append(bracket)

            else:

                #if stack is not empty ")[" or last added opening is not same type as closing
                if not stack or close_to_open[bracket] != stack[-1]:
                    return False
                
                #else, everything is fine, cancels out
                stack.pop()
        
        return not stack