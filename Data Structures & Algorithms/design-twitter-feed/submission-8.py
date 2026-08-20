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
        self.user_followers[userId].add(userId)

        max_heap = []  # use negative time for max-heap behavior

        # seed: newest tweet from each followee
        for cur_user in self.user_followers[userId]:
            tweets = self.user_tweets[cur_user]
            if tweets:
                index = len(tweets) - 1
                time_stamp, tweet_id = tweets[index]
                heapq.heappush(max_heap, (-time_stamp, tweet_id, cur_user, index))

        res = []
        while max_heap and len(res) < self.feed_limit:
            neg_time, tweet_id, cur_user, index = heapq.heappop(max_heap)

            next_index = index - 1
            res.append(tweet_id)
            if next_index >= 0:
                time_stamp, next_tweet_id = self.user_tweets[cur_user][next_index]
                heapq.heappush(max_heap, (-time_stamp, next_tweet_id, cur_user, next_index))

        return res

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
        
