class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])
        islands = 0

        def dfs_islands(r, c):

            if r < 0 or r >= rows or c < 0 or c >= columns or grid[r][c] == "0":
                return 
            
            #else

            grid[r][c] = "0"

            dfs_islands(r + 1, c)
            dfs_islands(r - 1, c)
            dfs_islands(r, c + 1)
            dfs_islands(r, c - 1)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    dfs_islands(r, c)
                    islands += 1
        
        return islands
