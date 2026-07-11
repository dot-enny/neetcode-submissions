class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, window = Counter(t), defaultdict(int)
        l, res, min_len, have = 0, [-1, -1], float('inf'), 0
        for r in range(len(s)):
            if s[r] in t_count:
                window[s[r]] += 1
                if window[s[r]] == t_count[s[r]]: have += 1

            while have == len(t_count):
                if (r - l + 1) < min_len:
                    res = [l, r]
                    min_len = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]: have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if min_len != float('inf') else  ""



            