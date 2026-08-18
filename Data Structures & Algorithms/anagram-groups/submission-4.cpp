class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;

        for (auto& str : strs) {
            vector<int> count(26, 0);
            for (auto& c : str) {
                count[c - 'a']++;
            }
            
            string key = "";
            for (auto& val : count) {
                key += to_string(val) + "_";
            }

            mp[key].push_back(str);
        }


        vector<vector<string>> res;
        for (auto& [key, val] : mp) {
            res.push_back(val);
        }

        return res;
    }
};
