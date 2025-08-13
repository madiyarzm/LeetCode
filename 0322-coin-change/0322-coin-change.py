class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dp(amount, coins):

            if amount == 0:
                return 0

            if amount < 0:
                return float('inf')

            if amount in memo:
                return memo[amount]

            else:
                answer = float('inf')

                for coin in coins:
                    subproblem = amount - coin

                    if subproblem < 0:
                        continue

                    answer = min(answer, dp(subproblem, coins) + 1)
            
            memo[amount] = answer

            return answer

        result = dp(amount,coins)

        if result == float('inf'): return -1

        return result