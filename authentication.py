import tweepy
from tweepy import StreamListener, Stream
import couchdb
import json

server = couchdb.Server('http://admin:admin@127.0.0.1:5984/')
db = server.create('test-twitter-5_17-test')

consumer_key = 'Twd11SLSUOhAvpmXq94bTUTtA'
consumer_secret = 'lVfoW9DHTnWPMp8h0CxJbMn0AzNf9J84gl5o5iQMfis6hGJG1r'

access_token = '1249239316515016704-k5Zkh6S1aYULx4MupRbPY45YABO4nH'
access_token_secret = 'LdQxM8DcdPS6QcsSmoRcUQmo8nWxs9B37VrpNFKY6pbLs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

AUSTRALIA = [112.35, -43.56, 154.41, -10.16]

try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepError:
    print('Error! Failed to get request token.')


class listener(StreamListener):

    def on_data(self, data):
        try:
            data_json = json.loads(data)
            if ("retweeted_status" not in data_json.keys()) and ("quoted_status" not in data_json.keys()) and data_json["lang"] == "en":
                tweet = dict()
                place = dict()
                hashtags = []
                tweet["created_at"] = data_json["created_at"]
                tweet["id"] = data_json["id_str"]
                tweet["user_screen_name"] = data_json["user"]["screen_name"]
                if "extended_tweet" not in data_json.keys():
                    tweet["text"] = data_json["text"]
                    if data_json["entities"]["hashtags"] is not None:
                        for i in data_json["entities"]["hashtags"]:
                            hashtags.append(i["text"])
                    tweet["hashtags"] = hashtags
                else:
                    tweet["text"] = data_json["extended_tweet"]["full_text"]
                    if data_json["extended_tweet"]["entities"]["hashtags"] is not None:
                        for i in data_json["extended_tweet"]["entities"]["hashtags"]:
                            hashtags.append(i["text"])
                    tweet["hashtags"] = hashtags
                if data_json["geo"] is not None:
                    tweet["geo"] = data_json["geo"]["coordinates"]
                tweet["geo"] = data_json["geo"]
                place["full_name"] = data_json["place"]["full_name"]
                place["country"] = data_json["place"]["country"]
                place["coordinates"] = data_json["place"]["bounding_box"]["coordinates"]
                tweet["place"] = place
                db.update([tweet])
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