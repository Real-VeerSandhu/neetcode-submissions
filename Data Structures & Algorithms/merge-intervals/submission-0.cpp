class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        /*

        [1,3], [8,10], [15, 18], [2,6]



        */

        sort(intervals.begin(), intervals.end());
        vector<vector<int>> output;

        output.push_back(intervals[0]);

        for (auto& interval : intervals) {
            int curStart = interval[0];
            int curEnd = interval[1];

            if (curStart <= output.back()[1]) {
                output.back()[1] = max(output.back()[1], curEnd);
            } else {
                output.push_back({curStart, curEnd});
            }
        }

        return output;


    }
};
