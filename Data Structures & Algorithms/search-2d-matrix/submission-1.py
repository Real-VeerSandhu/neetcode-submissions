class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m - 1

        search_row = 0

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target and target <= matrix[m][-1]:
                search_row = m
                break
            elif matrix[m][0] > target:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
        
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2

            if target < matrix[search_row][m]:
                r = m - 1
            elif target > matrix[search_row][m]:
                l = m + 1
            else:
                return True
        
        return False
