class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        res = [-1, -1]
        if not n: return res
        m = 0
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]: r = m - 1
            elif target > nums[m]: l = m + 1
            else: 
                res[0], res[1] = m, m
                break

        if nums[m] != target: return res

        l, r = m - 1, m + 1
        while (l > -1) and nums[l] == nums[m]: 
            res[0] -= 1
            l -= 1
        while (r < n) and nums[m] == nums[r]: 
            res[1] += 1
            r += 1

        return res