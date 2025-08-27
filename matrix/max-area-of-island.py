class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j] != 1:
                return
            grid[i][j] = 0
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    area += 1
                    max_area = max(max_area, area)
        return max_area