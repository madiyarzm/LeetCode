class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        #if min stack is not empty
        if self.min_stack:

            #append only currently min value to minstack
            val = min(val, self.min_stack[-1])
            self.min_stack.append(val)
        
        #if empty just add it
        else:
            self.min_stack.append(val)


    #you have to pop value from both stacks, to not have unexistent val from min_stack
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()