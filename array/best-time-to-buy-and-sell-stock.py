class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_bene = prices[0]
        best_bene = 0
        n = len(prices)
        for i in range(1, n):
            for j in range(i):
                if prices[i] - prices[j] > 0:
                    cur_bene = prices[i]-prices[j]
                    best_bene = max(best_bene, cur_bene)
        return best_bene
