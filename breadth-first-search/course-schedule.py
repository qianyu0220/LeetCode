class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegrees[a] += 1
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        count = 0
        while queue:
            cur = queue.popleft()
            count += 1
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    queue.append(nxt)
        return True if count == numCourses else False
