class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not mat1 or not mat2 or not mat1[0] or not mat2[0]:
            return []
        m = len(mat1)
        n = len(mat1[0])
        p = len(mat2[0])

        if len(mat2) != n:
            return []
        A_rows = []
        for i in range(m):
            row_dict = {}
            for k, val in enumerate(mat1[i]):
                if val != 0:
                    row_dict[k] = val
            A_rows.append(row_dict)
        B_rows = []
        for i in range(n):
            row_dict = {}
            for k, val in enumerate(mat2[i]):
                if val != 0:
                    row_dict[k] = val
            B_rows.append(row_dict)

        C = [[0] * p for _ in range(m)]

        for i in range(m):
            for k, a in A_rows[i].items():
                if not B_rows[k]:
                    continue
                for j, b in B_rows[k].items():
                    C[i][j] += a * b
        return C