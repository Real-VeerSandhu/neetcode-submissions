/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {

        vector<int> start;
        vector<int> end;

        for (const auto& i : intervals) {
            start.push_back(i.start);
            end.push_back(i.end);
        }

        sort(start.begin(), start.end(), less<int>());
        sort(end.begin(), end.end(), less<int>());

        int res = 0;
        int count = 0;
        int s = 0;
        int e = 0;

        while (s < intervals.size()) {
            if (start[s] < end[e]) {
                s++;
                count++;
            } else {
                e++;
                count--;
            }
            res = max(res, count);
        }

        return res;
    }
};
