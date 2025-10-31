class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        used = [False] * n
        def backtrack(path):
            if len(path) == n:
                output.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return output

