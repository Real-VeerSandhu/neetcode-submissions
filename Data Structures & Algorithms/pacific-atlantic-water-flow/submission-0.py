class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(grid)
        COLS = len(grid[0])
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        # bfs from pcf and atl -> needs to increase height each time or stay same

        def bfs(sources, ocean):
            q = deque(sources)


            while q:
                cur_r, cur_c = q.popleft()
                ocean[cur_r][cur_c] = True

                for dr, dc in dirs:
                    nr, nc = cur_r + dr, cur_c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] < grid[cur_r][cur_c] or ocean[nr][nc]:
                        continue
                    
                    q.append((nr, nc))
                    
        pacific = []
        atlantic = []

        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))
        
        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))
        
        bfs(pacific, pac)
        bfs(atlantic, atl)
        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        
        return res
                    
