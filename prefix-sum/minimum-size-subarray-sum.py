class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        output = float("inf")
        cur_sum = 0
        left = 0
        for right in range(1, n):
            cur_sum += nums[right]
            while cur_sum + nums[right] >= target:
                output = min(output, right-left+1)
                cur_sum -= nums[left]
                left += 1
        return output if output != float("inf") else 0