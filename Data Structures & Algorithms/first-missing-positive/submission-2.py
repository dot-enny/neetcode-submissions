class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # traverse
        # check, for values offset by 1
        # if it doesn't exist, save the smaller, non-existent, positive, non-zero to a variable
        # return variable
        res = 1
        nums_set = set(nums)

        def valid(val: int) -> bool:
            if (val not in nums_set) and (val > 0):
                return True

        for num in nums:
            prev = num - 1
            next = num + 1
            if valid(prev):
                res = res if valid(res) and res < prev else prev
            else:
                if valid(next):
                    res = res if valid(res) and res < next else next
        return res
