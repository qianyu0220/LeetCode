class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        benefit = 0
        for i in range(1, len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            benefit = max(benefit, prices[i] - buy_price)
        return benefit
