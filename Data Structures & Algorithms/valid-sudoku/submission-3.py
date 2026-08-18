class Board:
    def __init__(self, board_size, board):
        self.board_size = board_size
        self.square_size = int(self.board_size ** 0.5)
        self.board = board
        self.valid_items = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    
    def check_rows(self):
        for row in self.board:
            seen = set()
            for item in row:
                if item == '.':
                    continue
                if item not in self.valid_items:
                    return False
                if item in seen:
                    return False
                seen.add(item)
        
        return True
    
    def check_columns(self):
        for i in range(self.board_size):
            seen = set()
            for j in range(self.board_size):
                item = self.board[j][i]
                if item == '.':
                    continue
                if item not in self.valid_items:
                    return False
                if item in seen:
                    return False
                seen.add(item)
        
        return True
    
    
    def check_squares(self):
        for i in range(0, self.board_size, self.square_size):
            for j in range(0, self.board_size, self.square_size):
                seen = set()
                for x in range(i, i + self.square_size):
                    for y in range(j, j + self.square_size):
                        item = self.board[x][y]
                        if item == '.':
                            continue
                        if item not in self.valid_items:
                            return False
                        if item in seen:
                            return False
                        seen.add(item)
        return True
    
    def is_valid(self):
        return self.check_rows() and self.check_columns() and self.check_squares()


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        """
        row[r] -> maps row to its own set
        cols[c] sa,e


        square[(r, c)] ->

        r = 0,1,2
        -> r // square_size = 0
        -> c // square_size = 0

        r = 3,4,5
        -> r // square-size = 0
        
        """
        n = len(board)
        square_size = int(n ** 0.5)

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(n):
            for c in range(n):
                cell = board[r][c]

                if cell in rows[r] or cell in cols[c] or cell in squares[(r // square_size, c // square_size)]:
                    return False
                
                if cell == '.':
                    continue
                rows[r].add(cell)
                cols[c].add(cell)
                squares[(r // square_size, c // square_size)].add(cell)
    
        return True


        