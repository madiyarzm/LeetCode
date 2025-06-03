class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temp = x
        count = 0

        while temp > 0:
            temp = temp // 10
            count += 1

        i = 0
        

        while i < count:
            if x // (10 ** (count - i - 1)) % 10 != x // (10 ** i) % 10:
                return False

            i += 1

        return True