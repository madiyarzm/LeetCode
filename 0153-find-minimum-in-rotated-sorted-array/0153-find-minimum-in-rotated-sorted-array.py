class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """
        5 1 2 3 4 
        l   m   r

        l > r
            l > m
                m = l + m // 2
        
        4 5 1 2 3
        l   m   r
            
        l < r
            l > m
                return m
        
        3 4 5 6 1 2
        l.  m.     r

        l > r
            l < m
                m = m + r // 2
        
        5 1 2 3 4
        l.  m.   r

        l > r
            l > m
                m = l + m // 2
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[r]:
                return nums[l]

            elif nums[m] >= nums[l]:
                l = m + 1
            
            else:
                r = m