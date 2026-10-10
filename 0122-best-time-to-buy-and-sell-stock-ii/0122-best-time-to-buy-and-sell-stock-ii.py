class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        max_profit = 0
        hold = True
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                buy = prices[i]
            elif prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
