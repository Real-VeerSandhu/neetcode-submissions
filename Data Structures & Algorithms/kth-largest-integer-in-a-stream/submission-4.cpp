class KthLargest {
private:

    priority_queue<int, vector<int>, greater<int>> minHeap;
    int capacity = 0;

public:
    KthLargest(int k, vector<int>& nums) {
        capacity = k;
        for (int num : nums) {
            minHeap.push(num);
            if (minHeap.size() > capacity) {
                minHeap.pop();
            }
        }
    }
    
    int add(int val) {
        minHeap.push(val);

        if (minHeap.size() > capacity) {
            minHeap.pop();
        }

        return minHeap.top();
    }
};
