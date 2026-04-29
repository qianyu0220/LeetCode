class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        n = len(nums)
        for index, i in enumerate(nums):
            complement = target - i
            if complement in hashmap:
                return [hashmap[complement], index]
            else:
                hashmap[i] = index