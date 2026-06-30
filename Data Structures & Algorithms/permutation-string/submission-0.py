class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        for l in range(len(s2) - len(s1) + 1):
            sub = s2[l]
            for r in range(l + 1, l + len(s1)):
                sub += s2[r]
            if sorted(sub) == s1:
                return True
        return False
            

          

