class TicTacToe:

    def __init__(self, n: int):
        self.ROWS = n
        self.COLS = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        if (self._check_row(row, player)) or (self._check_col(col, player)) or (row == col and self._check_diag(player)) or (col == self.ROWS - row - 1 and self._check_anti_diag(player)):
            return player
        
        return 0
    
    def _check_row(self, row, player):
        for col in range(self.COLS):
            if self.board[row][col] != player:
                return False
        return True
    
    def _check_col(self, col, player):
        for row in range(self.ROWS):
            if self.board[row][col] != player:
                return False
        return True
    
    def _check_diag(self, player):
        for row in range(self.ROWS):
            if self.board[row][row] != player:
                return False
        return True

    def _check_anti_diag(self, player):
        for row in range(self.ROWS):
            if self.board[row][self.ROWS - 1 - row] != player:
                return False
        return True


"""
0: 0 1 2 3 4
1: 0 1 2 3 4
2: 0 1 2 3 4
3: 0 1 2 3 4
4: 0 1 2 3 4


"""

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
