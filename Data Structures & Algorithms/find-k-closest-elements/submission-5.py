class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k
        for c in arr[k:]:
            if abs(c - x) < abs(arr[l] - x):
                l, r = l + 1, r + 1
            elif abs(c - x) == abs(arr[l] - x) and arr[l] == c:
                l, r = l + 1, r + 1
        return arr[l:r]
                