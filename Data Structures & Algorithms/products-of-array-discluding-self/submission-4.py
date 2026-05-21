class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pref_arr, suff_arr = [1] * len(nums), [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            pref_arr[i] = prefix
            prefix*=nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            suff_arr[i] = suffix
            suffix*=nums[i]
        

        for i in range(len(nums)):
            res[i] = pref_arr[i] * suff_arr[i]
            
        return res

