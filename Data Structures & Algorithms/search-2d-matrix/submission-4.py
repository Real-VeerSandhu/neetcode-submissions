class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # first find correct ROW!!

        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[m][0] <= target <= matrix[m][COLS - 1]:
                break
            elif target > matrix[m][COLS - 1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
        
        row_index = m
        print(f'row index: {row_index}')

        l = 0
        r = COLS - 1

        while l <= r:
            m = (l + r) // 2

            if target == matrix[row_index][m]:
                return True
            elif target < matrix[row_index][m]:
                r = m - 1
            elif target > matrix[row_index][m]:
                l = m + 1
        
        return False
