class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)): 
            if cheap > prices[i]:
                cheap = prices[i]
            
            else:
                if maxProfit < prices[i] - cheap:
                    maxProfit = prices[i] - cheap
        
        return maxProfit