class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        output = 0
        n = len(nums)
        cur_sum = 0
        left = 0
        for right in range(n):
            cur_sum += nums[right]
            while (right - left + 1) - cur_sum > k:
                output = max(output, right - left)
                cur_sum -= nums[left]
                left += 1
                
        return output
