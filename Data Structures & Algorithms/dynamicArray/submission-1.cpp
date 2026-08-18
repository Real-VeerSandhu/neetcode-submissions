class DynamicArray {
public:
    int* arr_;
    int length_;
    int capacity_;

    DynamicArray(int capacity) {
        capacity_ = capacity;
        length_ = 0;
        arr_ = new int[capacity_];
    }

    int get(int i) {
        return arr_[i];
    }

    void set(int i, int n) {
        arr_[i] = n; 
    }

    void pushback(int n) {
        if (length_ == capacity_) {
            resize();
        }
        arr_[length_] = n;
        length_++;
    }

    int popback() {
        int value = arr_[length_ - 1];
        length_--;
        return value;
    }

    void resize() {
        int newCapacity = capacity_ * 2;
        int* newArr = new int[newCapacity];

        for (int i = 0; i < length_; i++) {
            newArr[i] = arr_[i];
        }

        delete[] arr_;
        arr_ = newArr;
        capacity_ = newCapacity;
    }

    int getSize() {
        return length_;
    }

    int getCapacity() {
        return capacity_;
    }
};
