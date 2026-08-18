class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> numMap;

        for (int i = 0; i < n; ++i) {
            if (numMap.count(target - nums[i])) {
                return {numMap[target - nums[i]], i};
            }
            numMap[nums[i]] = i;
        }
    }
};