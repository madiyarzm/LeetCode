class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #optimized DP iterative solution
        #assign our base case values, for ith step, its cost[i] and minimum from 2 choices
        #return cost for last 2 steps [-1], [-2]

        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):

            current = cost[i] + min(prev2, prev1)
            prev2 = prev1
            prev1 = current
        
        return min(prev2, prev1)