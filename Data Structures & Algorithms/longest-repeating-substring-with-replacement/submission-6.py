class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, res, max_f = 0, 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])

            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        '''
        s="AABABBA" k=1
        0: count[a] = 1, max = 1, res = 1
        1: count[a] = 2, max = 2, res = 2
        2: count[a,b] = [2,1], max = 2, res = 3
        3: count[a,b] = [3,1], max = 3, res = 4
        4: count[a,b] = [3,2], max = 3


        '''
