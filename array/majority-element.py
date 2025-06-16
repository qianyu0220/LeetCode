class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return [] 
        nums.sort()
        return nums[len(nums) // 2 + 1]
