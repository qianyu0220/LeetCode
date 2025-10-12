class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not mat1 or not mat2:
            return []
        m = len(mat1)
        n = len(mat1[0])
        p = len(mat2[0])
        row_A = []
        for i in range(m):
            row_dict = {}
            for k, val in enumerate(mat1[i]):
                if val != 0:
                    row_dict[k] = val
            row_A.append(row_dict)
        row_B = []
        for i in range(n):
            row_dict = {}
            for k, val in enumerate(mat2[i]):
                if val != 0:
                    row_dict[k]= val
            row_B.append(row_dict)
        C = [[0] * p for _ in range(m)]
        for i in range(m):
            for k, a in row_A[i].items():
                if not row_B[k]:
                    continue
                for j, b in row_B[k].items():
                    C[i][j] += a * b
        return C


            
