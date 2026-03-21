class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        n = len(nums)
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False