class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sequence = set(nums)


        mx = 0
    

        for number in sequence:
            
            lcs = 1

            if number - 1 not in sequence:
                while number + 1 in sequence:
                    lcs += 1
                    number = number + 1
                
                mx = max(mx, lcs)
        
        return mx