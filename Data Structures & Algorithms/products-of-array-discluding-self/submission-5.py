class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res, pref, suff = [0] * n, [0] * n, [0] * n

        pref[0] = suff[n - 1] = 1 #because index 0 has no prefix and the last index has no suffix

        for i in range(1, n): #starting from index 1
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1): #starting from the second to the last
            suff[i] = suff[i + 1] * nums[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
            
        return res

