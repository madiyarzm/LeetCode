import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1 
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        users_to_read = self.following[userId]

        all_tweets = list(self.tweets[userId])
        for user in users_to_read:
            all_tweets += self.tweets[user]

        tweet_heap = []
        for counter, tweetId in all_tweets:
            tweet_heap.append((-counter, tweetId))
        
        heapq.heapify(tweet_heap)

        result = []
        for i in range(min(len(tweet_heap), 10)):

            if i == 10:
                break

            negative_count, tweet = heapq.heappop(tweet_heap)
            result.append(tweet)
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)