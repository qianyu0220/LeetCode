class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n):
            left_ok = (i==0 or nums[i] - nums[i-1] > 1)
            right_ok = (i==n-1 or nums[i+1] - nums[i] > 1)
            if left_ok and right_ok:
                output.append(nums[i])
        return output