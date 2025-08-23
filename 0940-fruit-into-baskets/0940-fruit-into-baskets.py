class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        #this is the way to avoid key error (0)
        basket = collections.defaultdict(int)

        mx = 0
        total = 0

        l = 0
        for r in range(len(fruits)):

            basket[fruits[r]] += 1
            total += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                total -= 1
                
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                    
                l += 1

            mx = max(mx, total)
        
        return mx