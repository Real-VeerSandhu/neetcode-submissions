class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])

        self.row_prefix = [[0] * (self.COLS + 1) for _ in range(self.ROWS)]

        for r in range(self.ROWS):
            self._build_row(r)
        
    def _build_row(self, r):
        for c in range(self.COLS):
            self.row_prefix[r][c + 1] = self.row_prefix[r][c] + self.matrix[r][c]
        
        # row_prefix[r][1] = 3 means sum of everything in row r before col index 1 is 3
        print(f'built row: {r}', self.row_prefix[r])
    
    """
    0 1 2 3 4

    3 0 1 4 2
    """
    
    def _rebuild_row(self, r, c):
        for c in range(c, self.COLS):
            self.row_prefix[r][c + 1] = self.row_prefix[r][c] + self.matrix[r][c]

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        self._rebuild_row(row, col)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0

        for r in range(row1, row2 + 1):
            row_sum = self.row_prefix[r][col2 + 1] - self.row_prefix[r][col1]
            total += row_sum
        
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
