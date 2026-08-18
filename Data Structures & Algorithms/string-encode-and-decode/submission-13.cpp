class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";

        for (auto& str : strs) {
            int strLength = str.size();

            res += to_string(strLength) + '_' + str;

            // cout << "encode word: " << res << endl;
        }

        return res;
    }

    vector<string> decode(string s) {
        int i = 0;
        vector<string> res;

        while (i < s.size()) {
            int j = i;
            while (s[j] != '_') {
                j++;
            }
            /*
            1 5 0 _ z o o . . . 
            0 1 2 3 4 5 6
            */
            int length = stoi(s.substr(i, j - i));
            i = j + 1; // start of word
            res.push_back(s.substr(i, length));
            i += length;
        }

        return res;

    }
};
