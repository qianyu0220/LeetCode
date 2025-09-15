class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 1
        right = 1
        output = [1] * n
        for i in range(n):
            output[i] *= left
            left *= nums[i]
        for j in range(n-1, -1, -1):
            output[j] *= right
            right *= nums[j]
        return output