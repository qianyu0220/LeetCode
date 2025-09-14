class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        cur_min = 0
        for i in range(n):
            for j in range(i):
                max_profit = max(max_profit, prices[i] - prices[j])
        return max_profit