from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #create 9 sets for row and columns
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]

        #create default dictionary for automatic set creation
        grid = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": #skip if its empty
                    continue
                
                val = board[i][j]
                grid_key = (i // 3, j // 3) #get the grid key as a tuple of row and col position of the box

                if val in rows[i] or val in cols[j]: 
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                
                if val in grid[grid_key]: #(grid_i, grid_j) -> set()
                    return False

                grid[grid_key].add(val)
    
        return True
