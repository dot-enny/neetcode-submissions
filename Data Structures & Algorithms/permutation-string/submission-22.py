class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            r_char = ord(s2[r]) - ord("a")
            l_char = ord(s2[l]) - ord("a")

            # 2. Handle r_char (The one entering the window)
            if s2_count[r_char] == s1_count[r_char]: matches -= 1 # Was matched, now will be broken
            s2_count[r_char] += 1
            if s2_count[r_char] == s1_count[r_char]: matches += 1 # Was broken, now is matched
            # 1. Handle l_char (The one leaving the window)
            if s2_count[l_char] == s1_count[l_char]: matches -= 1 # Was matched, now will be broken
            s2_count[l_char] -= 1
            if s2_count[l_char] == s1_count[l_char]: matches += 1 # Was broken, now is matched

            l += 1
        
        return matches == 26
