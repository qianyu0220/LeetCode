class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1
        output = []
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                output.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            for i in range(top, bottom+1):
                output.append(matrix[i][right])
            right -= 1
            if left > right:
                break
            for i in range(right, left-1, -1):
                output.append(matrix[bottom][i])
            bottom -= 1
            if top > bottom:
                break
            for i in range(bottom, top-1, -1):
                output.append(matrix[i][left])
            left += 1
        return output

