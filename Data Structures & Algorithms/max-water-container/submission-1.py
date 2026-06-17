class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                h = heights[i] if heights[i] < heights[j] else heights[j]
                w = j - i
                amount = h * w
                res = amount if amount > res else res
        return res