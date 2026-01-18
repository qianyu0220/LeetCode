class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        nums_set = set(nums)
        n = len(nums_set)
        if n == len(nums):
            return False
        return True