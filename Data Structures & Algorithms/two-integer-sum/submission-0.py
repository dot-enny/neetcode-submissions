class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffCheck = {};
        result = [];
        for i, n in enumerate(nums):
            difference = target - n;
            if difference in diffCheck:
                return [diffCheck[difference], i];
            diffCheck[n] = i;
        return []