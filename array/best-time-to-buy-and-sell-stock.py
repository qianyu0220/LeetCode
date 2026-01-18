class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        n = len(prices)
        cur_profit = 0
        lowest = float("inf")
        for i in range(n):
            if prices[i] < lowest:
                lowest = prices[i]
            cur_profit = prices[i] - lowest
            output = max(output, cur_profit)
        return output
