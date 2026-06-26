class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, l = 0, 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len