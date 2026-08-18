class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int l = i + 1;
            int r = n - 1;
            while (l < r) {
                int curSum = nums[i] + nums[l] + nums[r];
                if (curSum == 0) {
                    res.push_back({nums[i], nums[l], nums[r]});
                    l += 1;
                    r -= 1;
                    while (l < r && nums[l] == nums[l - 1]) {
                        l += 1;
                    }
                } else if (curSum < 0) {
                    l += 1;
                } else {
                    r -= 1;
                }
            }
        }

        return res;
    }
};
