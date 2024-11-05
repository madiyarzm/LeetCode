#BFS, solving with 2 pointers, Greedy approach O(n)

class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 
        l = r = 0

        while r < len(nums) - 1:
            f = 0
            for i in range(l, r + 1):
                f = max(f, i + nums[i])
            
            l = r + 1
            r = f
            res = res + 1

        return res

