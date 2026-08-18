class MinStack {
private:
    vector<int> val_stack;
    vector<int> min_stack;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (val_stack.size() == 0) {
            val_stack.push_back(val);
            min_stack.push_back(val);
        } else {
            int newMin = min(val, min_stack.back());
            val_stack.push_back(val);
            min_stack.push_back(newMin);
        }
    }
    
    void pop() {
        val_stack.pop_back();
        min_stack.pop_back();
    }
    
    int top() {
        return val_stack.back();
    }
    
    int getMin() {
        return min_stack.back();
    }
};
