class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r, k = 1, 1, 1
        while l < len(nums) and r < len(nums):
            while nums[r] == nums[r - 1]:
                r += 1
                if r >= len(nums):
                    return k
            nums[l] = nums[r]
            l, r, k = l + 1, r + 1, k + 1
        return k