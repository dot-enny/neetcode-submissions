class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums);
        final_count = 0;
        for num in nums_set:
            if (num - 1) not in nums_set:
                count = 1;
                next = num + 1;
                while next in nums_set:
                    next+=1
                    count+=1
                if count > final_count:
                    final_count = count;
        return final_count