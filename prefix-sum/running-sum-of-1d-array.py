class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        cur_sum = 0

        for i in range(n):
            cur_sum += nums[i]
            output.append(cur_sum)
        return output