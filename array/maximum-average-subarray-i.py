class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = sum(nums[:k])
        output = cur_sum / k
        for i in range(k, n):
            cur_sum = cur_sum - nums[i-k] + nums[i]
            output = max(output, cur_sum/k)
        return output