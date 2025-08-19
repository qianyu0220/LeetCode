class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = defaultdict(int)
        pre = 0
        output = 0
        cur[0] = 1
        for x in nums:
            pre += x
            output += cur[pre - k]
            cur[pre] += 1
        return output 