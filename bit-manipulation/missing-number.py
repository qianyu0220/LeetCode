class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[-1] == n - 1:
            return n
        for i, num in enumerate(nums):
            if num != i:
                return i