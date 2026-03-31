class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        output = []
        for index, i in enumerate(nums):
            complement = target - i
            if complement in hashmap:
                return [index, hashmap[complement]]
            hashmap[i] = index