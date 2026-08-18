class Leaderboard {

private:
    unordered_map<int, int> scores;
public:
    Leaderboard() {
        
    }
    
    void addScore(int playerId, int score) {
        if (!scores.count(playerId)) {
            scores[playerId] = 0;
        }
        scores[playerId] += score;
    }
    
    int top(int K) {
        priority_queue<int, vector<int>, greater<int>> heap; // min heap

        for (const auto&[playerId, score] : scores) {
            heap.push(score);

            if (heap.size() > K) {
                heap.pop();
            }
        }

        int total = 0;
        while(heap.size()) {
            total += heap.top();
            heap.pop();
        }
        return total;
    }
    
    void reset(int playerId) {
        scores.erase(playerId);
    }
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */
