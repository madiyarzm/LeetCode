class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(cost) > sum(gas):
            return -1
    
        current_tank = 0
        total_tank = 0
        starting_index = 0

        for i in range(len(gas)):
            current_tank = current_tank + gas[i] - cost[i]
            total_tank = total_tank + gas[i] - cost[i]

            if current_tank < 0:
                current_tank = 0
                starting_index = i + 1
        """
        if total_tank < 0:
            return -1
        """

        return starting_index
                
