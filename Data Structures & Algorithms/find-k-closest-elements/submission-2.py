class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k
        for c in arr[k:]:
            if abs(c - x) < abs(arr[l] - x):
                l+=1
                r+=1
            # else:
            #     break
        return arr[l:r]
                

                