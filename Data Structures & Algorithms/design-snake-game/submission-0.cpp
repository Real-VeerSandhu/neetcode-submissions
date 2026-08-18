class SnakeGame {
    unordered_set<string> snakeSet;
    deque<pair<int, int>> snake;
    vector<vector<int>> food;
    int foodIndex;
    int width;
    int height;

    string pairToString(int row, int col) {
        return to_string(row) + "," + to_string(col);
    }

public:
    SnakeGame(int width, int height, vector<vector<int>>& food) {
        this->width = width;
        this->height = height;
        this->food = food;
        this->foodIndex = 0;
        this->snakeSet.insert(pairToString(0, 0)); // initially at [0][0]
        this->snake.push_back({0, 0});
    }

    int move(string direction) {
        pair<int, int> snakeCell = this->snake.front();
        int newHeadRow = snakeCell.first;
        int newHeadColumn = snakeCell.second;

        if (direction == "U") {
            newHeadRow--;
        } else if (direction == "D") {
            newHeadRow++;
        } else if (direction == "L") {
            newHeadColumn--;
        } else if (direction == "R") {
            newHeadColumn++;
        }

        pair<int, int> newHead = {newHeadRow, newHeadColumn};
        pair<int, int> currentTail = this->snake.back();

        // Boundary conditions.
        bool crossesBoundary1 = newHeadRow < 0 || newHeadRow >= this->height;
        bool crossesBoundary2 = newHeadColumn < 0 || newHeadColumn >= this->width;

        // Checking if the snake bites itself.
        bool bitesItself = this->snakeSet.count(pairToString(newHeadRow, newHeadColumn)) &&
                          !(newHead.first == currentTail.first && newHead.second == currentTail.second);

        // If any of the terminal conditions are satisfied, then we exit with rcode -1.
        if (crossesBoundary1 || crossesBoundary2 || bitesItself) {
            return -1;
        }

        // If there's an available food item and it is on the cell occupied by the snake after the move,
        // eat it.
        if ((this->foodIndex < this->food.size())
            && (this->food[this->foodIndex][0] == newHeadRow)
            && (this->food[this->foodIndex][1] == newHeadColumn)) {
            this->foodIndex++;
        } else {
            this->snake.pop_back();
            this->snakeSet.erase(pairToString(currentTail.first, currentTail.second));
        }

        // A new head always gets added
        this->snake.push_front(newHead);

        // Also add the head to the set
        this->snakeSet.insert(pairToString(newHeadRow, newHeadColumn));

        return this->snake.size() - 1;
    }
};