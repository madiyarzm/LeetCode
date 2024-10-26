class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        answer = []
        for num in nums:
            if num != val:
                answer.append(num)
        nums[:] = answer

            