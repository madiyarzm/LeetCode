class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn = float("inf")
        mx_profit = 0

        #we keep most cheapest stock so far
        for i in range(len(prices)):
            mn = min(mn, prices[i])

            #find max profit, by updating
            mx_profit = max(mx_profit, prices[i] - mn)
        
        return mx_profit