class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]