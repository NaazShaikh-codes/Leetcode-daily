class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - minimum

            if profit > max_profit:
                max_profit = profit

            if prices[i] < minimum:
                minimum = prices[i]

        return max_profit