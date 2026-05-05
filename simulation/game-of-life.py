class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), 
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                live_nei = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0<=x<m and 0<=y<n:
                        if board[x][y] == 1 or board[x][y] == 2:
                            live_nei += 1
                if board[i][j] == 1:
                    if live_nei < 2 or live_nei > 3:
                        board[i][j] = 2
                else:
                    if live_nei == 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
                


