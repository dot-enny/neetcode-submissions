class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) / 3;
        counts = collections.defaultdict(int);
        for i in range(len(nums)):
            counts[nums[i]]+=1

        result = [key for key, value in counts.items() if value > limit]
        return result
