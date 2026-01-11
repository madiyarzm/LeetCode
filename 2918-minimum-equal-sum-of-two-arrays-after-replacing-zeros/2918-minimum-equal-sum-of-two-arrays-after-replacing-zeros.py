class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        min_sum1 = sum(nums1) + nums1.count(0)
        min_sum2 = sum(nums2) + nums2.count(0)

        if not nums1.count(0) and not nums2.count(0):
            
            if min_sum1 != min_sum2:
                return -1
            
            return max(min_sum1, min_sum2)


        if not nums1.count(0):

            if min_sum1 < min_sum2:
                return -1
            
            else:
                return max(min_sum1, min_sum2)
        
        if not nums2.count(0):

            if min_sum1 > min_sum2:
                return -1
            
            else:
                return max(min_sum1, min_sum2)
        
        

        return max(min_sum1, min_sum2)