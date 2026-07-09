class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        #add to stack numbers, if operation seen, pull up TOP 2 numbers and operate on them, result goes back to stack
        for token in tokens:
            if token == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(operand1 + operand2)
                
            elif token == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(operand1 - operand2)
                
            elif token == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()

                stack.append(operand1 * operand2)
                
            elif token == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()
            
                #int() truncates toward zero (chops of decimals)
                #// goes down 1, like floot() in C++
                stack.append(int(operand1 / operand2)) 

            else:
                stack.append(int(token))
        
        return int(stack[0])