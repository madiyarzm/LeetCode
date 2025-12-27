class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn = float("inf")
        mx_profit = 0

        for i in range(len(prices)):
            mn = min(mn, prices[i])

            mx_profit = max(mx_profit, prices[i] - mn)
        
        return mx_profit