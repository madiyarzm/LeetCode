class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(start, combination, total):

            if target == total:
                res.append(list(combination))
                return
            
            elif target < total:
                return 
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, total + candidates[i])
                combination.pop()
        
        backtrack(0, [], 0)
        return res