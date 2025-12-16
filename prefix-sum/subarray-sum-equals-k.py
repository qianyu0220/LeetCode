class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        output = 0
        left = 0
        cur_sum = 0
        for right in range(n):
            cur_sum += nums[right]
            while cur_sum > k:
                
                cur_sum -= nums[left] 
                left += 1
            if cur_sum == k:
                output += 1
        return output
