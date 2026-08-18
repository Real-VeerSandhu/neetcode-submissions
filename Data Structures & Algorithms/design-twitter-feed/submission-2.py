class Twitter:

    def __init__(self):
        self.user_followers = defaultdict(set)
        self.user_posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_posts[userId].append([self.time, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.time += 1
        min_heap = []
        for followed_user in self.user_followers[userId]:
            # print('follwing', followed_user)
            # print('tweets:', self.user_posts[followed_user])
            for timestamp, tweet in self.user_posts[followed_user]:
                heapq.heappush(min_heap, [timestamp, tweet])
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
            
        # print('self user tweets:', self.user_posts[userId])
        for timestamp, tweet in self.user_posts[userId]:
            heapq.heappush(min_heap, [timestamp, tweet])
            if len(min_heap) > 10:
                heapq.heappop(min_heap)

        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        # print('res:', res)
        # print('***')
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        if followerId != followeeId:
            self.user_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        if followerId != followeeId and followeeId in self.user_followers[followerId]:
            self.user_followers[followerId].remove(followeeId)

