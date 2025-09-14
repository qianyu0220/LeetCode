class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        cur_min = float("inf")
        for i in range(n):
            if prices[i] < cur_min:
                cur_min = prices[i]
            elif prices[i] - cur_min > max_profit:
                max_profit = prices[i] - cur_min
        return max_profit