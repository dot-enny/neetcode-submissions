class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def canFindWindow(length):
            currSum = sum(nums[:length])
            if currSum >= target: return True
            for i in range(length, len(nums)):
                currSum += nums[i] - nums[i - length]
                if currSum >= target: return True
            return False

        low, high = 0, len(nums)
        res = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canFindWindow(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
