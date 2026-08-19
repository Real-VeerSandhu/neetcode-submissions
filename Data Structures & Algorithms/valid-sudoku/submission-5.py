class Solution:
    def rows_valid(self, board: List[List[str]]):
        for row in board:
            row_set = set()
            for num in row:
                if num != '.' and num in row_set:
                    return False
                row_set.add(num)
        
        return True


    def cols_valid(self, board: List[List[str]]):
        ROWS = len(board)
        COLS = len(board[0])

        for j in range(COLS):
            col_set = set()
            for i in range(ROWS):
                if board[i][j] != '.' and board[i][j] in col_set:
                    return False
                col_set.add(board[i][j])
        return True
    

    def squares_valid(self, board: List[List[str]]):
        n = len(board)
        square_size = int(n ** 0.5)

        assert(n == square_size * square_size)

        for i in range(0, n, square_size):
            for j in range(0, n, square_size):
                square_set = set()
                for x in range(i, i + square_size):
                    for y in range(j, j + square_size):
                        if board[x][y] != '.' and board[x][y] in square_set:
                            return False
                        square_set.add(board[x][y])
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.rows_valid(board) and self.cols_valid(board) and self.squares_valid(board)

