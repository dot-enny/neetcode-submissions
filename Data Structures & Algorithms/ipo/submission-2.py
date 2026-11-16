class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap = [(c, i) for i, c in enumerate(capital)]
        heapq.heapify(min_heap)
        max_heap = []
        
        while k and (min_heap or max_heap):

            while min_heap and min_heap[0][0] <= w:
                idx = heapq.heappop(min_heap)[1]
                heapq.heappush(max_heap, -profits[idx])

            if not max_heap: break
            
            w += -heapq.heappop(max_heap)
            k -= 1
        
        return w


