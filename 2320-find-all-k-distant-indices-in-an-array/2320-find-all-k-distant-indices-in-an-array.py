class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        indices = []

        for i in range(len(nums)):
            for j in range(max(0, i - k), min(i + k + 1, len(nums))):
                if nums[j] == key:
                    indices.append(i)
                    break
            

        return indices