class StockSpanner:

    def __init__(self):
        self.span = 1
        self.stack1 = []
        self.stack2 = []

    def next(self, price: int) -> int:
        self.span = 1
        while self.stack1 and self.stack1[-1] <= price:
            self.span += self.stack2[-1]
            self.stack1.pop()
            self.stack2.pop()
        self.stack1.append(price)
        self.stack2.append(self.span)
        print(self.stack1, self.stack2)
        return self.stack2[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)