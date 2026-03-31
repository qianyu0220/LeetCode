class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        output = 0
        lowest = prices[0]

        for i in range(n):
            lowest = min(lowest, prices[i])
            output = max(output, prices[i] - lowest)
        return output
