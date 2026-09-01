class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.score = 0
        self.snake_size = 1

        start_pos = (0, 0)
        
        self.snake_set = set()
        self.snake_set.add(start_pos)

        self.snake_q = deque()
        self.snake_q.append(start_pos)

        self.ROWS = height
        self.COLS = width

        self.food_q = deque()
        for r, c in food:
            self.food_q.append((r, c))
        
        self.dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

        self.r = 0
        self.c = 0

    def move(self, direction: str) -> int:
        dx, dy = self.dir_map[direction]

        new_r = self.r + dx
        new_c = self.c + dy

        if new_r < 0 or new_c < 0 or new_r == self.ROWS or new_c == self.COLS:
            return -1
        
        if self.food_q and new_r == self.food_q[0][0] and new_c == self.food_q[0][1]:
            food_r, food_c = self.food_q.popleft()
            self.snake_set.add((new_r, new_c))
            self.snake_q.append((new_r, new_c))

            self.r = new_r
            self.c = new_c

            self.score += 1
            return self.score

        tail_r, tail_c = self.snake_q.popleft()
        self.snake_set.remove((tail_r, tail_c))
        
        if (new_r, new_c) in self.snake_set:
            return -1
        
        self.snake_set.add((new_r, new_c))
        self.snake_q.append((new_r, new_c))

        self.r = new_r
        self.c = new_c

        return self.score
        



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
