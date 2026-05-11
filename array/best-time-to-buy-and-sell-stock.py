class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lowest = prices[0]
        output = 0
        for i in range(n):
            if prices[i] < lowest:
                lowest = prices[i]
            output = max(output, prices[i] - lowest)
        return output