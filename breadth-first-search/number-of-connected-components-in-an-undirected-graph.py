class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        def dfs(i):
            stack = [i]
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)
        count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                count += 1
        return count