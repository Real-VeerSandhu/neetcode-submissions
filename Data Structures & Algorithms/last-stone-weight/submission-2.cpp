class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {

        priority_queue<int, vector<int>, less<int>> maxHeap;
        for (auto& stone : stones) {
            maxHeap.push(stone);
        }

        while (maxHeap.size() > 1) {
            int first = maxHeap.top();
            maxHeap.pop();
            int second = maxHeap.top();
            maxHeap.pop();
            if (second < first) {
                maxHeap.push(first - second);
            }
        }

        maxHeap.push(0);
        return maxHeap.top();


    }
};
