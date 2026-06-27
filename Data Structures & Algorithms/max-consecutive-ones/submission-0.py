class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for r, num in enumerate(nums):
            if num == 1:
                count += 1
            if num == 0:
                count = 0
            res = max(count, res)
        return res