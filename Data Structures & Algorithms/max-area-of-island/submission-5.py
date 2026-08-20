class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            res = 1

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dx, dy in dirs:
                        new_r = r + dx
                        new_c = c + dy

                        if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] == 0:
                            continue
                        
                        grid[new_r][new_c] = 0
                        q.append((new_r, new_c))
                        res += 1
            
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, bfs(r, c))
        return res