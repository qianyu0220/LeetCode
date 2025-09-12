class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == target:
                return i
            if i < n and nums[i] < target < nums[i+1]:
                return i + 1
        if target > nums[-1]:
            return n

        else:
            return 0