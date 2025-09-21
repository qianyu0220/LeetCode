class Solution:
    def jump(self, nums: List[int]) -> int:
        output = 0
        farthest = 0
        cur_end = 0
        n = len(nums)
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                output += 1
                cur_end = farthest
        return output