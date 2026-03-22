class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        output = nums[0]
        for i in range(1, len(nums)):
            prev_max, prev_min = cur_max, cur_min
            cur_max = max(prev_max*nums[i], prev_min*nums[i], nums[i])
            cur_min = min(prev_max*nums[i], prev_min*nums[i], nums[i])
            output = max(output, cur_max)
        return output