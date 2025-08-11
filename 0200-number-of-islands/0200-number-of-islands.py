class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        def dfs_explore(r, c):
            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == "0":
                return 
            
            grid[r][c] = "0"

            #explore all directions
            dfs_explore(r + 1, c)
            dfs_explore(r - 1, c)
            dfs_explore(r, c + 1)
            dfs_explore(r, c - 1)
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    dfs_explore(i,j)
                    islands += 1
        
        return islands