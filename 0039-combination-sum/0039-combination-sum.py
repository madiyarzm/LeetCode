class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        #we can solve it using bruteforce/backtracking
        def backtrack(start, combination, total):
            
            #if we got our target value, just add the combination
            if target == total:
                res.append(list(combination))
                return
            
            #if we over it, then backtrack
            elif target < total:
                return 
            
            #to not count similar sequences twice, start from start pointer and further
            for i in range(start, len(candidates)):

                #add number and then pop it, after recursively checking over it
                combination.append(candidates[i])
                backtrack(i, combination, total + candidates[i])
                combination.pop()
        
        backtrack(0, [], 0)
        return res