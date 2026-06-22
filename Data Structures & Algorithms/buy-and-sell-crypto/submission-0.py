class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, max_profit = 0, 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[buy]
            if profit >= 0 and profit > max_profit:
                max_profit = profit
            elif prices[i] < prices[buy]:
                buy = i
        return max_profit
