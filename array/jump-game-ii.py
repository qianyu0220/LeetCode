class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReach = 0
        step = 0
        current = 0
        for i in range(len(nums)-1):
            maxReach = max(i+nums[i], maxReach)
            if current == i:
                step += 1
                current = maxReach
            elif current > len(nums) - 1:
                break
        return step
            