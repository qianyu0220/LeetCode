class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums)
        output = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 0
                while num+length in nums_set:
                    length += 1
                output = max(output, length)

        return output