class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
    
        for token in tokens:

            if token.lstrip('-').isdigit():
                stack.append(int(token))

            else:
                prev1 = stack.pop()
                prev2 = stack.pop()

                if token == "+":
                    stack.append(prev2 + prev1)

                if token == "-":
                    stack.append(prev2 - prev1)
                
                if token == "/":
                    stack.append(int(prev2 / prev1))
                
                if token == "*":
                    stack.append(prev2 * prev1)
        
        return stack[-1]