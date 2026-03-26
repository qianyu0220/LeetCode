class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        output = 0

        def dfs(a, b):
            if a<0 or a>=m or b<0 or b>=n or grid[a][b] != "1":
                return
            grid[a][b] = "0"
            dfs(a-1, b)
            dfs(a+1, b)
            dfs(a, b-1)
            dfs(a, b+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    output += 1
        return output