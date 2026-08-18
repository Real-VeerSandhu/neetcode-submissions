class SparseVector {
public:
    vector<pair<int, int>> pairs;
    
    SparseVector(vector<int> &nums) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                pairs.push_back({i, nums[i]});
            }
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
        int res = 0;
        int p = 0;
        int q = 0;

        while (p < pairs.size() && q < vec.pairs.size()) {
            if (pairs[p].first == vec.pairs[q].first) {
                res += pairs[p].second * vec.pairs[q].second;
                p++;
                q++;
            } else if (pairs[p].first > vec.pairs[q].first) {
                q++;
            } else {
                p++;
            }
        }

        return res;
    }
};

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);
