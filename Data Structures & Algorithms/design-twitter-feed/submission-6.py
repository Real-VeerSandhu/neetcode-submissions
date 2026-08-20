class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list) # maps user_id : (time_stamp, tweet_id)
        self.user_followers = defaultdict(set) # maps user_id : what other users they follow
        self.feed_limit = 10

    def _add_user(self, userId: int) -> None:
        if userId in self.user_followers:
            return
        self.user_followers

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.time += 1

        self.user_followers[userId].add(userId)

        min_heap = []

        for cur_user in self.user_followers[userId]:
            for time_stamp, tweet_id in self.user_tweets[cur_user]:
                heapq.heappush(min_heap, (time_stamp, tweet_id))

                if len(min_heap) > self.feed_limit:
                    heapq.heappop(min_heap)


        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        print(f'user={followerId} FOLLOWS user={followeeId}')
        print(f'user={followerId} watches posts of user={followeeId}')

        self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print(f'user={followerId} UNFOLLOWS user={followeeId}')
        print(f'user={followerId} STOPS watching posts of user={followeeId}')
        if followeeId not in self.user_followers[followerId]:
            return

        self.user_followers[followerId].remove(followeeId)
        
