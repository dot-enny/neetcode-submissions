class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.store[key]) - 1
        res = (float('inf'), '')
        
        while l <= r:
            m = (l + r) // 2
            t, v = self.store[key][m]
            if timestamp == t: res = (t, v) if t > res[0] else res
            if timestamp >= t: 
                res = (t, v) if abs(timestamp - t) < abs(timestamp - res[0]) else res
                l = m + 1
            else: r = m - 1

        return res[1]


