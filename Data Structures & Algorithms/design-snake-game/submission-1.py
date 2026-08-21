"""
give me feedback on this idea for lc question called design snake game


"""


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.dir_map = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
        self.food_q = deque()
        self.r = 0
        self.c = 0
        self.score = 0


        self.ROWS = height
        self.COLS = width

        for food_loc in food:
            self.food_q.append(food_loc)
        
        self.snake = deque()
        self.snake.append((0, 0))
        self.snake_set = set()
        self.snake_set.add((0, 0))
        self.snake_size = 1

    def move(self, direction: str) -> int:
        r, c = self.snake[0]
        dx, dy = self.dir_map[direction]
        new_r, new_c = r + dx, c + dy
        
        if new_r < 0 or new_c < 0 or new_r == self.ROWS or new_c == self.COLS:
            return -1

        if self.food_q and self.food_q[0][0] == new_r and self.food_q[0][1] == new_c:
   
            self.food_q.popleft()
            self.snake_size += 1
            self.score += 1
            self.snake.appendleft((new_r, new_c))
            self.snake_set.add((new_r, new_c))
        else:
            old_r, old_c = self.snake.pop()
            self.snake_set.remove((old_r, old_c))

            if (new_r, new_c) in self.snake_set:
                return -1
            
            self.snake.appendleft((new_r, new_c))
            self.snake_set.add((new_r, new_c))

        

        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
