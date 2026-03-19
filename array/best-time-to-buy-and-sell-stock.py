class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        best_benefit = 0
        n = len(prices)
        for i in range(n):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            if best_benefit < prices[i] - lowest_price:
                best_benefit = prices[i] - lowest_price
        return best_benefit