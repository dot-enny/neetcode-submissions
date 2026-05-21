class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        i = 0
        while i < len(nums):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            res[i] = product
            i+=1
        return res