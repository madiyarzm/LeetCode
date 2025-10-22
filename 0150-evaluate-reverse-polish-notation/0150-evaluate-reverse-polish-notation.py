class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        #we use stack structure

        stack = []
    
        for token in tokens:

            #if token is number, then push to stack
            if token.lstrip('-').isdigit():
                stack.append(int(token))

            #if token is not number -> operand
            else:

                #get the two last added numbers before operand
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
        
        #there should be only one value left
        return stack[-1]