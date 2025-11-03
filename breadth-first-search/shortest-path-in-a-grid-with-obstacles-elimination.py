class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[-1] * n for _ in range(m)]
        queue = deque([(0, 0, k, 0)])
        while queue:
            x, y, remain, steps = queue.popleft()
            if x == m-1 and y == n-1:
                return steps
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n:
                    nk = remain - grid[nx][ny]
                    if nk >= 0 and nk > visited[nx][ny]:
                        visited[nx][ny] = nk
                        queue.append((nx, ny, nk, steps+1))
        return -1