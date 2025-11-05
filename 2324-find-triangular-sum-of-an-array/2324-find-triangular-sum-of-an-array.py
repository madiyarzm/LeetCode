class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        result = nums.copy()

        while len(nums) > 1:

            #5
            for i in range(len(nums) - 1):

                #3 = 1 + 2
                result[i] = (nums[i] + nums[i+1]) % 10

            result.pop()
            nums = result


        return nums[0]