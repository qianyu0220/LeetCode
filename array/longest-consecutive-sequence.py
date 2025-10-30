class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums_set)
        if not nums:
            return 0
        output = 1
        length = 1
        for num in nums_set:
            if num+1 in nums_set:
                length += 1
            output = max(output, length)
        return output


