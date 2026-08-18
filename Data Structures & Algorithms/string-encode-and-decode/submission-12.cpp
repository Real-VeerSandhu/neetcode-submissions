class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";

        for (auto& str : strs) {
            int strLength = str.size();

            res += to_string(strLength) + "_" + str;

            // cout << "encode word: " << res << endl;
        }

        return res;
    }

    vector<string> decode(string s) {
        int i = 0;
        int n = s.size();

        vector<string> res;

        while (i < n) {
            
            string curWordDigits = "";
            int j = i;
            // traverse j to stard of word, and get curWord lenght;
            while (j < n && s[j] != '_') {
                curWordDigits += s[j];
                j++;
            }

            // cout << "cur word digi len chars:" << curWordDigits << endl;
            int curWordLength = 0;
            int base = 1;
            for (int k = curWordDigits.size() - 1; k >= 0; --k) {
                curWordLength += base * (int)(curWordDigits[k] - '0');
                base *= 10;
            }

            // cout << "cur word digi nums:" << curWordLength << endl;
            
            // j is at '_', word starts at j+1 and has curWordLength chars
            string curWord = s.substr(j + 1, curWordLength);
            res.push_back(curWord);

            // advance i past the word
            i = j + 1 + curWordLength;
        }



        return res;

    }
};
