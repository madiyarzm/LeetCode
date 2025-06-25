class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0 and n == 1:
            
            return False
                
        sm = n
        seen = set()
        current_sum = 0

        while True:
            
            #sm is not in set, so not false
            
            #number is 19
            number = sm

            while number > 0:
                
                #current sum is 9^2 + 1^2 = 81 + 1 = 82
                #print((number & 10) ** 2, " sms")
                current_sum = current_sum + (number % 10) ** 2
                number = number // 10
            
            #is current sum 1? no
            
            #print(current_sum, " numbers")
            if current_sum == 1:
                return True
            
            if sm in seen:
                return False
            
            #adding 19
            seen.add(sm)
            sm = current_sum
            current_sum = 0
                    