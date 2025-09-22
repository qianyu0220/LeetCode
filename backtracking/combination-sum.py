class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(start, path, cur_sum):
            if cur_sum == target:
                output.append(path[:])
                return 
            elif cur_sum > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, cur_sum + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return output