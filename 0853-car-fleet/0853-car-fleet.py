class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        hmap = {}

        for i in range(len(position)):
            hmap[position[i]] = (target - position[i]) / speed[i]
        
        position.sort()
        fleet = 0

        for i in range(len(position)):
            time = hmap[position[i]]

            while stack and stack[-1] <= time:
                stack.pop()
                
        
            stack.append(time)
    

        return len(stack)


