class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        m, n = len(image), len(image[0])
        def backtrack(i, j, grid):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if start_color != grid[i][j] or grid[i][j] == color:
                return
            grid[i][j] = color
            backtrack(i-1, j, grid)
            backtrack(i+1, j, grid)
            backtrack(i, j-1, grid)
            backtrack(i, j+1, grid)
        backtrack(sr, sc, image)
        return image