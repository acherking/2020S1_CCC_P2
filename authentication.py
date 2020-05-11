import tweepy
from tweepy import StreamListener, Stream


consumer_key = 'STg9AiiHgEodfdb42z8dUZZ8P'
consumer_secret = 'w2yd3WdmUp0KkBDUTnN45lYhXeTdT90Zf7K5ecv0L5wGgpEVrq'

access_token = '347241876-bKVHGw61pNHE8niRZk0lSvobvkcpqS09QbroLKCf'
access_token_secret = 'kjZwaOg6c8hB8P5tozn9NvAN5ePNR7sCD68yJrPAc7imh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

MELB = [144.7, -37.65, 144.85, -37.5]
AUSTRALIA = [112.35, -43.56, 154.41, -10.16]

try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepError:
    print('Error! Failed to get request token.')

class listener(StreamListener):

    def on_data(self, data):
        try:
            print(data)
            #这里把data存到couchdb中就可以了
            return True
        except BaseException as e:
            print(e)
            return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        # returning False in on_data disconnects the stream
        if status_code == 420:
            print(status_code)
            return False



twitterStream = Stream(auth=auth, listener=listener())
twitterStream.filter(locations=AUSTRALIA)


"""
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    
#melbourne areas   

"""
