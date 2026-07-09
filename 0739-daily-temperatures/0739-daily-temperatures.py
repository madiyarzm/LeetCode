class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []

        #create result array to where we will place based on the index of temperature, not append
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            
            #stack is non empty and its monotonic  decreasing
            while stack and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1] #since its indexes, be careful here
                stack.pop() 
            
            stack.append(i)
        
        return result
