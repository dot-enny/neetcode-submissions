class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(nums);
        counts = [];
        count = 1;
        for i in range(1, len(sorted_nums)):
            diff = sorted_nums[i] - sorted_nums[i - 1]
            if diff < 2:
                if diff == 0:
                    continue
                count+=1;
            else:
                counts.append(count);
                count = 1;
        counts.append(count);
        return max(counts)

            


        