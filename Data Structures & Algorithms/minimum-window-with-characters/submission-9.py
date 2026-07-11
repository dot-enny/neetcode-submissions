class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        need = Counter(t)
        window = {}
        
        # 'have' is the number of unique characters that meet the 'need'
        have, need_total = 0, len(need)
        res, min_len = [-1, -1], float('inf')
        
        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            # If this character is needed and we just hit the required count
            if char in need and window[char] == need[char]:
                have += 1
            
            # While the window is valid, try to shrink it
            while have == need_total:
                # Update the smallest result
                if (r - l + 1) < min_len:
                    res = [l, r]
                    min_len = r - l + 1
                
                # Shrink: remove s[l] from window
                left_char = s[l]
                window[left_char] -= 1
                
                # If we were relying on that char, the window is now invalid
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]+1] if min_len != float('inf') else ""