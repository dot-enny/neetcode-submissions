class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        deDup = set(nums);
        if len(deDup) == len(nums):
            return False;
        return True;
        