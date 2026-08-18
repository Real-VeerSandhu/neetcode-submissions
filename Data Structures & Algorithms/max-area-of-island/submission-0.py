class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        visit = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0 or (r, c) in visit:
                return 0
            
            visit.add((r, c))

            return (1 + \
                dfs(r + 1, c)+
                dfs(r - 1, c)+
                dfs(r, c + 1)+
                dfs(r, c - 1)
                )
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        
        return res

            
