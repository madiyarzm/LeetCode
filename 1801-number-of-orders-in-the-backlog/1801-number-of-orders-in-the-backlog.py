import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        
        buys = []
        sells = []

        def matching(buys, sells):
            """
            helper function that takes buy and sell order lists

            returns nothing, changes in place
            """

            #make sure they are not empty, and price of buy is larger than sell
            while buys and sells and buys[0][0] * -1 >= sells[0][0]:

                #get highest buy orders, and lowest sell orders
                buy_price, buy_amount = heapq.heappop(buys)
                sell_price, sell_amount = heapq.heappop(sells)

                #which amount is lesser
                matched = min(buy_amount, sell_amount)

                #execute, or substract the orders
                buy_amount -= matched
                sell_amount -= matched

                #if there were more buy orders, put them back to the log
                if buy_amount > 0:
                    heapq.heappush(buys, (buy_price, buy_amount))
                
                #vice versa
                elif sell_amount > 0:
                    heapq.heappush(sells, (sell_price, sell_amount))


        #creating 2 heaps, based on priority of price
        for price, amount, act in orders:

            #if its buying order
            if not act:
                heapq.heappush(buys, (-price, amount))

                #match until its possible by "greedy middleman principle"
                matching(buys, sells)

            #if its selling order
            else:
                heapq.heappush(sells, (price, amount))
                matching(buys, sells)
            
        
        def sum_amount(lst):
            backlog = 0
            for price, amount in lst:
                backlog += amount
        
            return backlog

        mod = 10**9 + 7
            
        return (sum_amount(buys) + sum_amount(sells)) % mod
