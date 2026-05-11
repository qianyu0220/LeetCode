class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lowest = prices[0]
        output = 0
        for index, i in enumerate(prices):
            if i < lowest:
                lowest = i
            output = max(output, i - lowest)
        return output

