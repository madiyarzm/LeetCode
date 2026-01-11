class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    grids[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(i, j):
            if i == 9:
                return True
            
            if j == 9:
                return backtrack(i + 1, 0)
            
            if board[i][j] != ".":
                return backtrack(i, j + 1)
            
            grid_id = (i // 3) * 3 + j // 3

            for num in map(str, range(1, 10)):
                if num not in rows[i] and num not in cols[j] and num not in grids[grid_id]:
                    board[i][j] = num
                    rows[i].add(num)
                    cols[j].add(num)
                    grids[grid_id].add(num)

                    if backtrack(i, j + 1):
                        return True

                    # undo (backtrack)
                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    grids[grid_id].remove(num)

            return False
        
        backtrack(0, 0)
        



            

        
        