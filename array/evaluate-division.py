class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1/ val
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for nxt, val in graph[start].items():
                if nxt not in visited:
                    res = dfs(nxt, end, visited)
                    if res != -1.0:
                        return res * val
            return -1.0

        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))
        return ans