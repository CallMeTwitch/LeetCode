class Solution:
    def maxProfit(self, prices):
        holding = False
        profit = 0
        buy = 0

        for q in range(len(prices) - 1):
            if prices[q] < prices[q + 1] and holding == False:
                buy = prices[q]
                holding = True
            elif prices[q] > prices[q + 1] and holding == True:
                holding = False
                profit += prices[q] - buy
        if holding:
            profit += prices[-1] - buy

        return profit