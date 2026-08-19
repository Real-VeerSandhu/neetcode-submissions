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
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)

        ROWS = len(board)
        COLS = len(board[0])

        assert(ROWS == COLS)
        
        square_size = ROWS ** 0.5

        assert(square_size ** 2 == ROWS)

        for r in range(ROWS):
            for c in range(COLS):
                cur = board[r][c]
                if cur == '.':
                    continue
                if cur in row_map[r] or cur in col_map[c] or cur in square_map[(r // square_size, c // square_size)]:
                    return False
                row_map[r].add(cur)
                col_map[c].add(cur)
                square_map[(r // square_size, c // square_size)].add(cur)

        return True