class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        rows, columns = len(matrix), len(matrix[0])
        cache = {}


        def helper(i, j):
            if i >= rows or j >= columns:
                return 0
            
            if (i, j) not in cache:
                down = helper(i + 1, j)
                right = helper(i, j + 1)
                diag = helper(i + 1, j + 1)

                cache[(i, j)] = 0
                
                if matrix[i][j] == "1":
                    cache[(i, j)] = 1 + min(down, right, diag)
                

            return cache[(i, j)]
        
        helper(0, 0)
        return max(cache.values()) ** 2
