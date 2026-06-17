class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            h = heights[l] if heights[l] < heights[r] else heights[r]
            w = r - l
            amount = h * w
            res = amount if amount > res else res
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l, r = l + 1, r - 1
        return res