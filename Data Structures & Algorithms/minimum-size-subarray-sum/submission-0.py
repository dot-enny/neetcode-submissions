class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, prefix_sum, res = 0, nums[0], 0
        if nums[0] >= target: return 1
        for r in range(1, len(nums)):
            prefix_sum += nums[r]
            while prefix_sum >= target:
                res = (min(res, r - l + 1) if res > 0 else r - l + 1)
                prefix_sum -= nums[l]
                l += 1
        return res

