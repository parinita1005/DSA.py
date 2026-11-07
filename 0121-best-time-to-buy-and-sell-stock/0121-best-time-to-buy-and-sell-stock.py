class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_prices = float("inf")
        n = len(prices)
        for i in range(0,n):
            min_prices = min(min_prices,prices[i])
            max_profit = max(max_profit,prices[i]-min_prices)
        return max_profit
        