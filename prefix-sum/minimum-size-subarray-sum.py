class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        left = 0
        n = len(nums)
        window_sum = 0
        for right in range(n):
            window_sum += nums[right]
            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if ans==float("inf") else ans
