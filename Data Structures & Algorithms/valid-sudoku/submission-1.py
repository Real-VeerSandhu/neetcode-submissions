class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqs = defaultdict(set)

        SIZE = 9

        for r in range(SIZE):
            for c in range(SIZE):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in sqs[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqs[(r//3,c//3)].add(board[r][c])
        
        return True
        

                

