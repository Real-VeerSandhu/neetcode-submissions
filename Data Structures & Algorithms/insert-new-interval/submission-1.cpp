class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;

        int newStart = newInterval[0];
        int newEnd = newInterval[1];

        int n = intervals.size();

        for (int i = 0; i < n; i++) {
            if (intervals[i][0] > newEnd) {
                // we've reached an interval that starts AFter newInterval ends
                // therefore intervals[i] and all after it do not overlap
                // add newInterval then rest of intervals
                res.push_back(newInterval);
                for (int j = i; j < n; j++) {
                    res.push_back(intervals[j]);
                }
                return res;
            } else if (intervals[i][1] < newStart) {
                // intervals[i] ends beofre newInterval start. therefore this one is just
                // before newInterval, add it and keep going
                res.push_back(intervals[i]);
            } else {
                // occurs when intervals[i][0] <= newEnd
                // AND intervals[i][1] >= newStart

                newInterval[0] = min(newInterval[0], intervals[i][0]);
                newInterval[1] = max(newInterval[1], intervals[i][1]);
            }
        }
        res.push_back(newInterval);
        return res;
    }
};
