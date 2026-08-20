class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        atl = [[False] * COLS for _ in range(ROWS)]
        pac = [[False] * COLS for _ in range(ROWS)]

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(ocean, sources):
            q = deque(sources)
            

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    
                    for dx, dy in dirs:
                        new_r = r + dx
                        new_c = c + dy

                        if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] < grid[r][c] or ocean[new_r][new_c] == True:
                            continue
                        
                        q.append((new_r, new_c))
                        ocean[new_r][new_c] = True
        
        atl_start = []
        pac_start = []

        for c in range(COLS):
            pac_start.append((0, c))
            atl_start.append((ROWS - 1, c))

            pac[0][c] = True
            atl[ROWS - 1][c] = True

        for r in range(ROWS):
            pac_start.append((r, 0))
            atl_start.append((r, COLS - 1))

            pac[r][0] = True
            atl[r][COLS - 1] = True
        
        bfs(pac, pac_start)
        bfs(atl, atl_start)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        
        return res

