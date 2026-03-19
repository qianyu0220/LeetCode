class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lowest = prices[0]
        benefit = 0
        for i in range(n):
            lowest = min(lowest, prices[i])
            benefit = max(benefit, prices[i] - lowest)
        return benefit