class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def dfs_t(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return 
            
            board[r][c] = "T"

            dfs_t(r + 1, c)
            dfs_t(r - 1, c)
            dfs_t(r, c + 1)
            dfs_t(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i in [0, ROWS - 1] or j in [0, COLS - 1]):
                    dfs_t(i,j)

        def dfs_capture(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return 
            
            board[r][c] = "X"

            dfs_capture(r + 1, c)
            dfs_capture(r - 1, c)
            dfs_capture(r, c + 1)
            dfs_capture(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    dfs_capture(r,c)
                
                if board[r][c] == "T":
                    board[r][c] = "O"
