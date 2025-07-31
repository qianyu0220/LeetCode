class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        window_sum = 0
        ans = float('inf')
        for right in range(n):
            window_sum += nums[right]

            while window_sum >= target:
                ans = min(ans, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if ans == float('inf') else ans
                