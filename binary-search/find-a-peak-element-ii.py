class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n-1
        output = []
        while left <= right:
            mid = (left + right) // 2
            max_row = 0
            max_cur = 0
            for i in range(m):
                if mat[i][mid] > max_cur:
                    max_cur = mat[i][mid]
                    max_row = i
            left_val = mat[max_row][mid-1] if mid-1>=0 else -1
            right_val = mat[max_row][mid+1] if mid+1 < n else -1

            if mat[max_row][mid] > left_val and mat[max_row][mid] >right_val:
                return [max_row, mid]
            elif mat[max_row][mid] < left_val:
                right = mid - 1
            else:
                left = mid + 1

