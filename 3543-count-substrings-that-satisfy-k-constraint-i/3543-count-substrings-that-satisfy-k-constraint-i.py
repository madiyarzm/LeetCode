class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        zeroes = 0
        ones = 0

        l = 0
        r = 1

        for r in range(len(s)):

            if s[r] == '0':
                zeroes += 1
            
            else:
                ones += 1

            while zeroes > k and ones > k:

                if s[l] == '0':
                    zeroes -= 1
                
                else:
                    ones -= 1

                l += 1
            
            count += (r - l + 1)
        
        return count
            
