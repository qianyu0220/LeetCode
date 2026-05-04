class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        output = [[0] * n for _ in range(m)]
        directions = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy
                    if 0<=x<m and 0<=y<n:
                        total += img[x][y]
                        count += 1
                output[i][j] = total // count
        return output