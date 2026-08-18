class HitCounter {
private:
    queue<int> hits;
public:
    HitCounter() {
        
    }
    
    void hit(int timestamp) {
        hits.push(timestamp);
    }
    
    int getHits(int timestamp) {
        while (!hits.empty()) {
            int diff = timestamp - hits.front();
            if (diff >= 300) hits.pop();
            else break;
        }
        return hits.size();
    }
};

/*
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.



t1, t2, t3, t300

getHits(300) -> [0, 300], all need > 0 and <= 300
getHits(301) -> [1, 301], all need > 1 and <= 300



*/

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */
