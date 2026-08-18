class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            time += 1
            for _ in range(len(q)):
                cur_r, cur_c = q.popleft()

                for dr, dc in dirs:
                    nr = cur_r + dr
                    nc = cur_c + dc

                    if nc < 0 or nr < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr,nc))
        
        return time if fresh == 0 else -1