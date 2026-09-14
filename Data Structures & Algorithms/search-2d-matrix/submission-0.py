class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, r1 = 0, len(matrix) - 1
        while l1<=r1:
            m1 = (l1 + r1) // 2
            l2, r2 = 0, len(matrix[m1]) - 1
            m2 = 0
            while l2 <= r2:
                m2 = (l2 + r2) // 2
                if target < matrix[m1][m2]: r2 = m2 - 1
                elif target > matrix[m1][m2]: l2 = m2 + 1
                else: return True
            if target < matrix[m1][m2]: r1 = m1 - 1
            elif target > matrix[m1][m2]: l1 = m1 + 1

        return False