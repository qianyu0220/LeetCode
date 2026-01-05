class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = len(edges)
        output = 1
        for i in range(m):
            if i>0 and edges[i][0] != edges[i-1][1]:
                output += 1
        return output