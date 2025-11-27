class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        cur_profit = 0
        for i in range(n):
            for j in range(i, n):
                cur_profit = prices[j] - prices[i]
                if cur_profit > max_profit:
                    max_profit = cur_profit
        return max_profit