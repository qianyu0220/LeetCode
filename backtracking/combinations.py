class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        path = []
        def backtrack(start):
            if len(path) == k:
                output.append(path[:])
                return 
            for i in range(start, n+1):
                path.append(i)
                backtrack(i+1)
                path.pop()
        backtrack(1)
        return output