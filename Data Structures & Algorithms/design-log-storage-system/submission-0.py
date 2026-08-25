class LogSystem:

    def __init__(self):
        self.store = []
        self.gran_map = {
            "Year": 0, 
            "Month": 1, 
            "Day": 2, 
            "Hour": 3, 
            "Minute": 4, 
            "Second": 5
        }

    def put(self, id: int, timestamp: str) -> None:
        year, month, day, hour, minute, second = timestamp.split(':')
        
        self.store.append([[ year, month, day, hour, minute, second], id])

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        gran_index = self.gran_map[granularity] + 1

        start_trunc = ''.join(start.split(':')[:gran_index])
        end_trunc = ''.join(end.split(':')[:gran_index])

        res = []

        for ts, id in self.store:
            if start_trunc <= ''.join(ts[:gran_index]) <= end_trunc:
                res.append(id)
        
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
