class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, max = 1, 4 => 3, 4 => 3, 7
        # before making any decision, look ahead by 1 space, and check if you have previously bought
        # if price[i + 1] < price[i]: don't buy, move from i to i+1, 7 to 1
        # if price[i + 1] > price[i]: buy i, buy 1
        # if we have bought we can only sell or move ahead
        # if price[i + 1] < price[i]: sell i, sell 5
        # profit = prices[i] - prices[buy] = 5 - 1 = 4
        # we've sold, now we can, B|S|M
        # 3 is lower than 6 so buy 3
        # sell at 6, because 4 is lower than 6
        # profit = 6 - 3 = 3, new max = 4 + 3 = 7
        # buy, max = 1, 0
        buy, max = None, 0
        for i in range(len(prices) - 1):
            if buy == None:
                if prices[i + 1] > prices[i]:
                    buy = i
            else:
                if prices[i + 1] < prices[i]:
                    profit = prices[i] - prices[buy]
                    max += profit
                    buy = None
        if buy != None:
            print(prices[len(prices) - 1], prices[buy])
            max += prices[len(prices) - 1] - prices[buy]
        return max

            
            
                

