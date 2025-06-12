class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefits = []
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                benefit = prices[j] - prices[i]
                benefits.append(benefit)
        return max(benefits)
