from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sorted_scores = SortedDict() # sorts in ascending order, so max would be reverse aka * -1
        # sorted_scores is a freq map!! key is negative, val is freq

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sorted_scores[-score] = self.sorted_scores.get(-score, 0) + 1
        else:
            prev_score = self.scores[playerId]
            prev_val = self.sorted_scores.get(-prev_score)
            if prev_val == 1:
                del self.sorted_scores[-prev_score]
            else:
                self.sorted_scores[-prev_score] = prev_val - 1
            
            new_score = prev_score + score
            self.scores[playerId] = new_score
            self.sorted_scores[-new_score] = self.sorted_scores.get(-new_score, 0) + 1

    def top(self, K: int) -> int:
        count, total = 0, 0

        for key, value in self.sorted_scores.items():
            freq = self.sorted_scores.get(key)

            for _ in range(freq):
                total += -key
                count += 1

                if count == K:
                    break
            
            if count == K:
                break
        
        return total

    def reset(self, playerId: int) -> None:
        prev_score = self.scores[playerId]

        if self.sorted_scores[-prev_score] == 1:
            del self.sorted_scores[-prev_score]
        else:
            self.sorted_scores[-prev_score] -= 1
        del self.scores[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
