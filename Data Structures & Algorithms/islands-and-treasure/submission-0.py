from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit = set()
            visit.add((r,c))

            distance = 0
            while len(q) > 0:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    if grid[r][c] == 0:
                        return distance

                    nei = [[0,1], [1,0], [0,-1], [-1,0]]
                    
                    for y, x in nei:
                        rf = r + y
                        cf = c + x

                        if min(rf,cf) < 0 or rf >= ROWS or cf >= COLS or grid[rf][cf] == -1 or (rf,cf) in visit:
                            continue
                        q.append((rf,cf))
                        visit.add((rf,cf))
                distance += 1
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2147483647:
                    out = bfs(r,c)
                    if out != False:
                        grid[r][c] = out