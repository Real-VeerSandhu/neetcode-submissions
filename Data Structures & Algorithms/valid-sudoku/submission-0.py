class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def search_square(x, y):
            print('-------ssq------')
            seen = set()

            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    print(board[i][j], ' ',end='')
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
                print()
            return True

        SIZE = 9

        for i in range(SIZE):
            row_set = set()

            for j in range(SIZE):
                print(board[i][j], ' ',end='')
                if board[i][j] == '.':
                    continue
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j])
            print()
        
        for i in range(SIZE):
            col_set = set()

            for j in range(SIZE):
                print(board[j][i], end='')
                if board[j][i] == '.':
                    continue
                if board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])
            print()

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                print(i, j)
                if not search_square(i, j):
                    return False


        return True
        

                

