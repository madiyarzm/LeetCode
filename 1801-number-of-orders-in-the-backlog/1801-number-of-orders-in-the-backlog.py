import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        
        buys = []
        sells = []

        def matching(buys, sells):
            while buys and sells and buys[0][0] * -1 >= sells[0][0]:
                buy_price, buy_amount = heapq.heappop(buys)
                sell_price, sell_amount = heapq.heappop(sells)

                matched = min(buy_amount, sell_amount)

                buy_amount -= matched
                sell_amount -= matched

                if buy_amount > 0:
                    heapq.heappush(buys, (buy_price, buy_amount))
                
                elif sell_amount > 0:
                    heapq.heappush(sells, (sell_price, sell_amount))


        #creating 2 heaps, based on priority of price
        for price, amount, act in orders:
            if not act:
                heapq.heappush(buys, (-price, amount))
                matching(buys, sells)

            
            else:
                heapq.heappush(sells, (price, amount))
                matching(buys, sells)
            
        
        backlog = 0

        for price, amount in buys:
            backlog += amount

        for price, amount in sells:
            backlog += amount
            
        return backlog % (10**9 + 7)
