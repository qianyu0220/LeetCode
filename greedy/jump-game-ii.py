class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        output = 0
        farthest = 0
        cur_end = 0
        for i in range(n-1):
            farthest = max(farthest, nums[i] + i)
            if cur_end == i:
                cur_end = farthest
                output += 1
        return output