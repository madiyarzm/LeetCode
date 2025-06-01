class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        we are using 2 pointers technique here
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        """
        start backwards to avoid overriding, since nums1 is larger
        """
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            
            else:
                nums1[k] = nums1[i]
                i -= 1
            
            k -= 1
        
        """
        if we keep skipping nums2 elements, we might need to finish placing them
        """
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        
        return nums1



                