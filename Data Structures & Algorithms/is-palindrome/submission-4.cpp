class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l <= r) {
            if (!alphaNum(s[l])) l++;
            else if (!alphaNum(s[r])) r--;
            else {
                if (tolower(s[l]) != tolower(s[r])) return false;
                l++;
                r--;
            }
        }

        return true;
    }

    bool alphaNum(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z') || (c >= '0' && c <= '9');
    }
};
