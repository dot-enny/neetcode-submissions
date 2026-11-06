class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [( -1 * (((p[0] ** 2) - 0) + ((p[1] ** 2) - 0)), i) for i, p in enumerate(points)]
        heapq.heapify(distances)
        
        res = []
        while len(distances) > k:
            heapq.heappop(distances)

        for d, i in distances:
            res.append(points[i])

        return res
