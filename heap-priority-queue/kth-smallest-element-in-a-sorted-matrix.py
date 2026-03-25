class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        new = []
        for i in range(n):
            for j in range(n):
                new.append(matrix[i][j])
        new.sort()
        return new[-n*n + k - 1]