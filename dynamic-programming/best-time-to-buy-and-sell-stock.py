class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best_price = prices[0]
        output = 0
        for i in range(n):
            if prices[i] < best_price:
                best_price = prices[i]
            output = max(output, prices[i] - best_price)
        return output