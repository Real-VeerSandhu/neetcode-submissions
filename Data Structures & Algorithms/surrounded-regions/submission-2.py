class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dx, dy in dirs:
                        new_r = r + dx
                        new_c = c + dy

                        if min(new_r, new_c) < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != 'O':
                            continue
                        grid[new_r][new_c] = 'Y'
                        q.append((new_r, new_c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (c == 0 or c == COLS - 1 or r == 0 or r == ROWS - 1) and grid[r][c] == 'O':
                    # print('r, c', r, c)
                    grid[r][c] = 'Y'
                    bfs(r, c)
        # print(grid)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
                if grid[r][c] == 'Y':
                    grid[r][c] = 'O'
        
