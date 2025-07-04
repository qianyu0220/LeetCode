class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        current_end = 0
        farthest = 0
        n = len(nums)
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if current_end == i:
                step += 1
                current_end = farthest
            elif current_end > n - 1:
                break
        return step