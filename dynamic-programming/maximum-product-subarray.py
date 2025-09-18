class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = nums[0], nums[0]
        output = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            prev_max, prev_min = cur_max, cur_min
            cur_max = max(x, x * prev_max, x * prev_min)
            cur_min = min(x, x * prev_max, x * prev_min)
            output = max(cur_max, output)
        return output