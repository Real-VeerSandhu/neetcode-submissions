class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet;

        for (auto& num : nums) {
            numSet.insert(num);
        }

        int res = 0;

        for (auto& num : numSet){
            if (!numSet.count(num - 1)) {
                // start of seqneces;
                int cur = num;
                while (numSet.count(cur)) {
                    cur++;
                }
                res = max(res, cur - num);
            }
        }

        return res;
    }
};
