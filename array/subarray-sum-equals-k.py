class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        output = 0
        pre = 0
        cur = defaultdict(int)
        cur[0] = 1
        for x in nums:
            pre += x
            output += cur[pre-k]
            cur[pre] += 1
        return output
