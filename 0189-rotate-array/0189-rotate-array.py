class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = len(nums)
        k = k % j
        i = j - k
        
        nums[:] = nums[i:j] + nums[0:i]
        