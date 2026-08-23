class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # first find correct ROW!!

        """
        0 1 2 3 4
        0 1 2 3 4
        
        
        0 1 2 3 4
        5 6 7 8 9


        """

        ROWS = len(matrix)
        COLS = len(matrix[0])

        l = 0
        r = ROWS * COLS - 1

        while l <= r:
            m = (l + r) // 2

            row = m // COLS
            col = m % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1
        return False


