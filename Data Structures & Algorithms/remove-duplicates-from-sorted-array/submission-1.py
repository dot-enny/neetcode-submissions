class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## input - array in ascending order
        ## remove the duplicates in place
        ## space - 0(n)
        ## output - number of unique elements k
        left = 1;
        right = 1;
        
        while right < (len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right];
                left+=1
                right+=1
            else:
                right+=1;
        return left