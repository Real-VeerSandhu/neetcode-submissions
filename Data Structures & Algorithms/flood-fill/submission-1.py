class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        start_colour = image[sr][sc]

        def dfs(r, c, visit):
            if r < 0 or c < 0 or r == ROWS or c == COLS or image[r][c] != start_colour or (r,c) in visit:
                return
            
            visit.add((r,c))
            image[r][c] = color

            dfs(r + 1, c, visit)
            dfs(r - 1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c - 1, visit)
            visit.remove((r,c))

            return
        
        dfs(sr, sc, set())
        
        return image
