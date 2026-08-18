class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();

        unordered_map<int, int> freqMap;

        for (auto& num : nums) {
            freqMap[num]++;
        }

        vector<vector<int>> freqs(n + 1);

        for (auto& [key, val] : freqMap) {
            freqs[val].push_back(key);
        }

        vector<int> res;

        for (int i = freqs.size() - 1; i > 0; i--) {
            if (!freqs[i].size()) continue;

            for (auto& f : freqs[i]) {
                res.push_back(f);
                k--;
                if (!k) return res;
            }
        }

        return res;
    }
};
