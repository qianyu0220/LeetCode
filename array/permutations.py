class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        used = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                output.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return output