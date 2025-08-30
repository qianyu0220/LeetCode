class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_bene = prices[0]
        best_bene = 0
        n = len(prices)
        for i in range(1, n):
            for j in range(i):
                if prices[i] - prices[j] > 0:
                    best_bene = max(best_bene, prices[i]-prices[j])
        return best_bene
