class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while 0<=i<=m-1 and 0<=j<=n-1:
            val = matrix[i][j]
            if val == target:
                return True
            elif val < target:
                j += 1
            else:
                i -= 1
        return False