class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        m, n = len(image), len(image[0])
        def backtracking(i, j, grid):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == color:
                return
            if grid[i][j] != start_color:
                return 
            grid[i][j] = color
            backtracking(i+1, j, grid)
            backtracking(i-1, j, grid)
            backtracking(i, j+1, grid)
            backtracking(i, j-1, grid)
        backtracking(sr, sc, image)
        return image

