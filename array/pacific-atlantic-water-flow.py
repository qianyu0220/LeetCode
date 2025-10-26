class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(i, j, visited):
            visited.add((i, j))
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                if 0<=x<m and 0<=y<n:
                    if (x, y) not in visited and heights[x][y] >= heights[i][j]:
                        dfs(x,y,visited)
        pacific = set()
        atlantic = set()
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)
        for i in range(m):
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(m-1, j, atlantic)
        return list(pacific & atlantic)