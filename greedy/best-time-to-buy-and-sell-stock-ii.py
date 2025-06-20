class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = [0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                #buy_price = prices[i]
                profit = profit + (prices[i] - prices[i-1])
            elif prices[i] < prices[i-1]:
                buy_price = prices[i]
        return profit

            