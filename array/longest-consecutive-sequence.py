class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)
        output = 1
        if not nums:
            return 0

        for num in nums:
            if num + 1 in nums:
                output += 1
        return output
