class Solution:
    def isValid(self, s: str) -> bool:
        
        #matching closing to opening parenthesis
        pars = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for i in range(len(s)):

            #if its closing bracket, check whether top of the stack is its match
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                
                if len(stack) == 0 or pars[stack[-1]] != s[i]: #if stack is empty, then closer appears before
                    return False
                
                else:
                    stack.pop() #after match remove opener from stack
                    continue
                
            stack.append(s[i]) #if its opening, then add it to stack
        
        return len(stack) == 0
            