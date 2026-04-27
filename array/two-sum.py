class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        output = []
        hashmap = {}
        for index, i in enumerate(nums):
            complement = target - i
            if complement in hashmap:
                return [index, hashmap[complement]]
            else:
                hashmap[i] = index