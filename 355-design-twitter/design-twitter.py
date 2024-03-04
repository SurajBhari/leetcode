class Twitter:

    def __init__(self):
        self.tweets = [] # [[user, tweet_id]]
        self.ff = [] # [[a,b]] a follows b
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        # get the people user follows
        follows = [x[1] for x in self.ff if x[0] == userId]
        follows.append(userId)
        count =0
        returning = []
        for tweet in self.tweets[::-1]:
            if tweet[0] not in follows:
                continue
            else:
                returning.append(tweet[1])
            count += 1
            if count == 10:
                break
        return returning
            
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.ff.append([followerId, followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.ff.remove([followerId, followeeId])
        except ValueError:
            pass

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)