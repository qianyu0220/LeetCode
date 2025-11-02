class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        left = 0
        right = n - 1

        while left <= right:
            mid = (left+right) // 2
            max_row = 0
            cur_max = mat[0][mid]
            for i in range(m):
                if i > 0 and mat[i][mid] > cur_max:
                    max_row = i
                    cur_max = mat[i][mid]
            if mid - 1 >= 0:
                left_val = mat[max_row][mid-1]
            else:
                left_val = -1
            if mid + 1 < n:
                right_val = mat[max_row][mid+1]
            else:
                right_val = -1
            if mat[max_row][mid] > left_val and mat[max_row][mid] > right_val:
                return [max_row, mid]
            elif mat[max_row][mid] < left_val:
                right = mid - 1
            else:
                left = mid + 1


