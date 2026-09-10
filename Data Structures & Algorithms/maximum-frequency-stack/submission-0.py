class FreqStack:

    def __init__(self):
        self.levels = defaultdict(list)
        self.max_freq = defaultdict()
        self.highest_freq = 0

    def push(self, val: int) -> None:
        if val in self.max_freq: self.max_freq[val] += 1
        else: self.max_freq[val] = 1
        self.levels[self.max_freq[val]].append(val)
        self.highest_freq = max(self.highest_freq, self.max_freq[val])

    def pop(self) -> int:
        if not len(self.levels[self.highest_freq]):
            self.highest_freq -= 1
        self.max_freq[self.levels[self.highest_freq][-1]] -= 1
        return self.levels[self.highest_freq].pop()


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()