class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = collections.defaultdict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in check:
                return [check[complement], i]
            else:
                check[nums[i]] = i