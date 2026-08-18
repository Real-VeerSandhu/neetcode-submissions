class Twitter:

    def __init__(self):
        self.user_posts = defaultdict(list)
        self.user_followers = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.user_followers[userId].add(userId)
        for followeeId in self.user_followers[userId]:
            if followeeId in self.user_posts: 
                index = len(self.user_posts[followeeId]) - 1
                count, tweetId = self.user_posts[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])
            
        while min_heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.user_posts[followeeId][index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_followers[followerId]:
            self.user_followers[followerId].remove(followeeId)

