class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        
        for number in nums:
            if number in unique:
                return True
            unique.add(number)
        return False