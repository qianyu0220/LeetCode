class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        def dfs(i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i, j+1) + dfs(i,j-1)

        max_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_island = max(max_island, dfs(i,j))
        return max_island