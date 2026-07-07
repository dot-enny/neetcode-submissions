class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = arr[:k]
        l = 0
        for r in arr[k:]:
            if abs(r - x) < abs(arr[l] - x):
                res.pop(0)
                l+=1
                res.append(r)
        return res
                

                