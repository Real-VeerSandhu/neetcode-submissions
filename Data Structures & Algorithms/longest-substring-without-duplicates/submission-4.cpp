class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> seen;
        int res = 0;
        int l = 0;

        for (char& c : s) {
            while (seen.count(c)) {
                seen.erase(s[l]);
                l+=1;
            }
            seen.insert(c);
            res = max(res, (int)seen.size());
        }

        return res;
    }
};
