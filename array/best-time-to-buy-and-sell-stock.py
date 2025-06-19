class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        benefit = 0

        for i in prices[1:]:
            if buy_price > i:
                buy_price = i

            benefit = max(benefit, i - buy_price)
        return benefit

