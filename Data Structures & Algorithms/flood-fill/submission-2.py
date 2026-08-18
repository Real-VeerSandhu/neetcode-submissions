class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        start_colour = image[sr][sc]

        if color == start_colour:
            return image

        def dfs(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or image[r][c] != start_colour:
                return
            
            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return
        
        dfs(sr, sc)
        
        return image
