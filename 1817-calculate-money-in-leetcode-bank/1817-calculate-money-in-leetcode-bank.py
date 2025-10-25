class Solution:
    def totalMoney(self, n: int) -> int:

        total = 0
        money = 1
        starter = 1


        for day in range(n):
            
            total += money

            money += 1

            if (day + 1) % 7 == 0:
                
                starter += 1
                money = starter


        return total

                