class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dx, dy in dirs:
                        new_r, new_c = r + dx, c + dy

                        if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] == '0':
                            continue
                        
                        grid[new_r][new_c] = '0'
                        q.append((new_r, new_c))
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    bfs(r, c)
        
        return res