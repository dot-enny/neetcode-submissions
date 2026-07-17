class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        def is_integer(val):
            try:
                int(val)
                return True
            except ValueError:
                return False

        for i, c in enumerate(operations):
            n = len(record) - 1
            if is_integer(c):
                record.append(int(c))
                last = int(c)
            elif c == '+':
                record.append(int(record[n]) + int(record[n - 1]))
            elif c == 'D':
                record.append(record[n] * 2)
            elif c == 'C':
                record.pop()
            print(record)
        return sum(record)
        
        
