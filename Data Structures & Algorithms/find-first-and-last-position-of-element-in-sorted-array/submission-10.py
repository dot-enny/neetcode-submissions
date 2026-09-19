class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(is_first: bool):
            l, r = 0, len(nums) - 1
            idx = -1

            while l <= r:
                m = (l + r) // 2
                if target == nums[m]:
                    idx = m
                    if is_first: r = m - 1
                    else: l = m + 1
                elif target < nums[m]: r = m - 1
                else: l = m + 1

            return idx
    
        return [findBound(True), findBound(False)]