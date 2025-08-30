class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best_price = prices[0]
        output = 0
        for i in range(1, n):
            if prices[i] < best_price:
                best_price = prices[i]
            output = max(prices[i] - best_price, output)
        return output