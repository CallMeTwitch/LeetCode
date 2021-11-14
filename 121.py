class Solution:
    def maxProfit(self, prices):
        best = 0
        current = prices[0]
        for q in range(1, len(prices)):
            if prices[q] > current:
                best = max(prices[q] - current, best)
            else:
                current = prices[q]

        return best