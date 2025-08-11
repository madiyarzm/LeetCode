class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original_color = image[sr][sc]
        if original_color == color:
            return image

        m = len(image)
        n = len(image[0])

        def dfs_flood(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != original_color:
                return
            
            image[i][j] = color

            dfs_flood(i + 1,j)
            dfs_flood(i - 1,j)
            dfs_flood(i,j + 1)
            dfs_flood(i,j - 1)

            return image
        
        return(dfs_flood(sr,sc))