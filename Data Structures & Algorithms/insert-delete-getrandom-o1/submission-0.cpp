class RandomizedSet {
private:
    unordered_map<int, int> numMap;
    vector<int> nums;


public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if (numMap.count(val)) return false;

        numMap[val] = nums.size();
        nums.push_back(val);
        return true;
    }
    
    bool remove(int val) {
        if (!numMap.count(val)) return false;

        int indexOld = numMap[val];
        int endVal = nums.back();

        nums[indexOld] = endVal;
        numMap[endVal] = indexOld;

        nums.pop_back();
        numMap.erase(val);

        return true;
    }
    
    int getRandom() {
        return nums[rand() % nums.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */