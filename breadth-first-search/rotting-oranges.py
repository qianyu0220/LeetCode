class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0
        while queue:
            r, c, minutes = queue.popleft()
            for dr, dc in directions:
                
                nr, nc = dr+r, dc+c
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr,nc,minutes+1))
        return -1 if fresh>0 else minutes
