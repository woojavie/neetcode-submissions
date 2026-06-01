class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
        m = (l + r) // 2
        l0, r0 = 0, len(matrix[m]) - 1
        while l0 <= r0:
            m0 = (l0 + r0) //2
            if target > matrix[m][m0]:
                l0 = m0 + 1
            elif target < matrix[m][m0]:
                r0 = m0 - 1
            else:
                return True
        return False