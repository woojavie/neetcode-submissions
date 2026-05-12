class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l,r = 0, len(matrix[m]) - 1
                while l <= r:
                    m0 = (l + r) // 2
                    if target > matrix[m][m0]:
                        l = m0 + 1
                    elif target < matrix[m][m0]:
                        r = m0 - 1
                    else:
                        return True
        return False