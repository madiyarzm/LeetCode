class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mn = float('inf')
        mx_profit = 0

        for price in prices:
            mn = min(mn, price) #keep track of cheapest 
            mx_profit = max(mx_profit, price - mn) #update max profit by difference
        
        return mx_profit