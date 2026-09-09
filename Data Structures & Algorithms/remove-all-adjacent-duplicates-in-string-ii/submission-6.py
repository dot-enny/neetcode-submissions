class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stores (char, current_consecutive_count) tuples
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        res = []
        for c in stack:
            char, count = c
            res.append(char * count)
        return ''.join(res)