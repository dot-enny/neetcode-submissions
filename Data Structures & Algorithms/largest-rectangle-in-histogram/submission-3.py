class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height) pair
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (i - index) * height)
                start = index
            stack.append((start, h))
        
        n = len(heights)
        for i, h in stack:
            max_area = max(max_area, (n - i) * h)
        
        return max_area


