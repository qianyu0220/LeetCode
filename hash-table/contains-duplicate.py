class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in nums_set:
                return True
            else:
                nums_set.add(nums[i])
        return False