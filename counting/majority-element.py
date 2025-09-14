class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        mid = (0 + len(nums) - 1) // 2
        return nums[mid]