class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        n = len(prices)
        for i in range(1, n):
            if prices[i] < prices[i-1]:
                buy_price = prices[i]
            elif prices[i] >= prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
