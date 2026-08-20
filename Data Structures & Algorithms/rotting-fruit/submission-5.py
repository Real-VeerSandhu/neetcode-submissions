class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0
        fresh_fruits = 0

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        
        # visit will be avoided by just modified grid!!

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh_fruits += 1
        
        while q and fresh_fruits > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

        
                
                for dx, dy in dirs:
                    new_r = r + dx
                    new_c = c + dy

                    if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or grid[new_r][new_c] != 1:
                        continue
                    fresh_fruits -= 1
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
            res += 1

        return res if fresh_fruits == 0 else -1