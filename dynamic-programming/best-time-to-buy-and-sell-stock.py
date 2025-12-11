class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        output = 0
        cur_profit = 0
        for i in range(n):
            for j in range(i+1, n):
                cur_profit = prices[j] - prices[i]
                output = max(output, cur_profit)
        return output
