class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mx = float('-inf')
        sell = 0

        for i in range(len(prices)):
            mx = max(mx,-prices[i])
            sell = max(sell, mx + prices[i])
        
        return sell