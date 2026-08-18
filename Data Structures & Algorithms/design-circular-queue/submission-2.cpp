class MyCircularQueue {

private:
    int front = 0;
    int rear = -1;
    int size = 0;
    vector<int> q;
    int capacity;
public:
    MyCircularQueue(int k) {
        capacity = k;
        q = vector<int> (capacity, -1);
    }

    /*

        8 9 X X X X X
        0 1 2 3 4 5 6


    */
    
    bool enQueue(int value) {
        if (isFull()) return false;
        
        rear = (rear + 1) % capacity;
        q[rear] = value;
        size++;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;

        q[front] = -1;
        front = (front + 1) % capacity;
        size--;
        return true;
    }
    
    int Front() {
        if (isEmpty()) return -1;
        return q[front];
    }
    
    int Rear() {
        if (isEmpty()) return -1;
        return q[rear];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == capacity;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */