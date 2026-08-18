class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.grid = []

        for _ in range(n):
            self.grid.append([0] * n)

    def move(self, row: int, col: int, player: int) -> int:
        self.grid[row][col] = player

        if self.row_check(row, player) or self.col_check(col, player):
            return player
        
        if row == col and self.diag_check(player):
            return player
        
        if col == self.n - row - 1 and self.anti_diag_check(player):
            return player
        
        return 0


    def row_check(self, row, player):
        for col in range(self.n):
            if self.grid[row][col] != player:
                return False
        return True

    def col_check(self, col, player):
        for row in range(self.n):
            if self.grid[row][col] != player:
                return False
        return True

    def diag_check(self, player):
        
        for row in range(self.n):
            if self.grid[row][row] != player:
                return False
        return True
    
    def anti_diag_check(self, player):

        for row in range(self.n):
            if self.grid[row][self.n - row - 1] != player:
                return False
        return True


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
