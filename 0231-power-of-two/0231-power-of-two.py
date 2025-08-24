import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        #we have to input validate & edge check
        if n <= 0:
            return False

        #logariphms in python are float error prone, thats why, we check this way
        return 2 ** int(math.log(n, 2)) == n
    