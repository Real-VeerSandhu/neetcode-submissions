class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_colour = image[sr][sc]
        if color == start_colour:
            return image


        ROWS = len(image)
        COLS = len(image[0])
        q = deque()
        q.append((sr, sc))
        image[sr][sc] = color

        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == start_colour:
                        image[nr][nc] = color
                        q.append((nr, nc))
        
        return image