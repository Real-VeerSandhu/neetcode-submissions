class TimeMap {
private:

    unordered_map<string, vector<pair<int, string>>> mp;
public:
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        mp[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {

        /*
            say we have this: [1, 3, 5, 9, 10, 12, 14]

            if we search for 5, we just return 5 -> idx -> val.second

            if we search for 6, we will need to do binary search such that we end up at 5

        */

        auto& vec = mp[key];

        int l = 0;
        int r = vec.size() - 1;
        int ans = -1;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (vec[mid].first == timestamp) return vec[mid].second;
            else if (vec[mid].first < timestamp) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return ans == -1 ? "" : vec[ans].second;
    }
};
