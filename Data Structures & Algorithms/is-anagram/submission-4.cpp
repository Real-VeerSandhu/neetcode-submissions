class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        vector<int> keyS(26, 0);
        vector<int> keyT(26, 0);

        for (const auto& c : s) {
            keyS[c - 'a']++;
        }
        for (const auto& c : t) {
            keyT[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (keyS[i] != keyT[i]) {
                return false;
            }
        }

        return true;


    }
};
