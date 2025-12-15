class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        output = cur_sum / k
        n = len(nums)
        for i in range(k, n):
            cur_sum = cur_sum - nums[i-k] + nums[i]
            output = max(output, cur_sum / k)
        return output