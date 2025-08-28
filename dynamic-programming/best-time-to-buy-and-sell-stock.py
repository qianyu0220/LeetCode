class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        benefit = 0
        for i in range(len(prices)):
            if prices[i] < buy_price:
                buy_price = prices[i]
            benefit = max(benefit, prices[i]-buy_price)
        return benefit