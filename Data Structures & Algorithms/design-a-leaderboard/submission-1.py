class Leaderboard:

    def __init__(self):
        self.leaderboard = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.leaderboard:
            self.leaderboard[playerId] += score
        else:
            self.leaderboard[playerId] = score
        


    def top(self, K: int) -> int:
        res = 0
        minheap = []

        for player_id, score in self.leaderboard.items():
            minheap.append((score, player_id))
        heapq.heapify(minheap)
        
        while len(minheap) > K:
            heapq.heappop(minheap)

        for score, _ in minheap:
            res += score
        return res

    def reset(self, playerId: int) -> None:
        del self.leaderboard[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
