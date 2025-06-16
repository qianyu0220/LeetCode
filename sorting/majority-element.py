class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return [] 
        nums.sort()
        n = len(nums)
        return nums[n // 2 + 1]
