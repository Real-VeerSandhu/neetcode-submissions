class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        area = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]


        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
      
        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            res = 1

            while q:
                for _ in range(len(q)):
                    r1, c1 = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = r1 + dr, c1 + dc
                        if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0:
                            continue
                        grid[nr][nc] = 0
                        res += 1
                        q.append((nr, nc))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area