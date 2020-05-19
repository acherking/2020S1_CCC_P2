import json
import tweepy
import time
import couchdb
import threading
from datetime import datetime
from textblob import TextBlob
from tweepy import StreamListener, Stream
from urllib3.exceptions import ProtocolError

server = couchdb.Server('http://admin:123456@172.26.131.241:5984/')
db = server.create('australia_5_20_1')

#server = couchdb.Server('http://admin:admin@127.0.0.1:5984/')
#db = server.create('test-australia_5_18')

consumer_key = 'STg9AiiHgEodfdb42z8dUZZ8P'
consumer_secret = 'w2yd3WdmUp0KkBDUTnN45lYhXeTdT90Zf7K5ecv0L5wGgpEVrq'

access_token = '347241876-84TA0mSNVeYHqBSNierhpYkvVnpIjn6srvzf6feR'
access_token_secret = 'fHgAw0JsBvE9wgShh0auAdVsGWkp8wtAFFiDUofazGbwS'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

MELBOURNE = [144.30, -38.30, 145.50, -37.30]
AUSTRALIA = [112.35, -43.56, 154.41, -10.16]
AUSTRALIA_CITY = {'Australian Capital Territory': ['Canberra'], 'New South Wales': ['Tuncurry', 'Silverdale - Warragamba', 'Silverdale', 'Warragamba', 'Albury', 'Armidale', 'Ballina', 'Balranald', 'Batemans Bay', 'Bathurst', 'Bega', 'Bourke', 'Bowral', 'Broken Hill', 'Byron Bay', 'Camden', 'Campbelltown', 'Cobar', 'Coffs Harbour', 'Cooma', 'Coonabarabran', 'Coonamble', 'Cootamundra', 'Corowa', 'Cowra', 'Deniliquin', 'Dubbo', 'Forbes', 'Forster', 'Glen Innes', 'Gosford', 'Goulburn', 'Grafton', 'Griffith', 'Gundagai', 'Gunnedah', 'Hay', 'Inverell', 'Junee', 'Katoomba', 'Kempsey', 'Kiama', 'Kurri Kurri', 'Lake Cargelligo', 'Lismore', 'Lithgow', 'Maitland', 'Moree', 'Moruya', 'Murwillumbah', 'Muswellbrook', 'Nambucca Heads', 'Narrabri', 'Narrandera', 'Newcastle', 'Bomaderry', 'Nowra', 'Orange', 'Parkes', 'Parramatta', 'Penrith', 'Port Macquarie', 'Queanbeyan', 'Raymond Terrace', 'Richmond', 'Scone', 'Singleton', 'Sydney', 'Tamworth', 'Taree', 'Temora', 'Tenterfield', 'Tumut', 'Ulladulla', 'Wagga Wagga', 'Wauchope', 'Wellington', 'West Wyalong', 'Windsor', 'Wollongong', 'Wyong', 'Yass', 'Young'], 'Northern Territory': ['Alice Springs', 'Anthony Lagoon', 'Darwin', 'Katherine', 'Tennant Creek'], 'Queensland': ['Ayr', 'Beaudesert', 'Blackwater', 'Bowen', 'Brisbane', 'Buderim', 'Bundaberg', 'Caboolture', 'Cairns', 'Charleville', 'Charters Towers', 'Cooktown', 'Dalby', 'Deception Bay', 'Emerald', 'Gatton', 'Gladstone', 'Gold Coast', 'Goondiwindi', 'Gympie', 'Hervey Bay', 'Ingham', 'Innisfail', 'Kingaroy', 'Mackay', 'Mareeba', 'Maroochydore', 'Maryborough', 'Moonie', 'Moranbah', 'Mount Isa', 'Mount Morgan', 'Moura', 'Redcliffe', 'Rockhampton', 'Roma', 'Stanthorpe', 'Toowoomba', 'Townsville', 'Warwick', 'Weipa', 'Winton', 'Yeppoon'], 'South Australia': ['Crafers', 'Adelaide', 'Ceduna', 'Clare', 'Coober Pedy', 'Gawler', 'Goolwa', 'Iron Knob', 'Leigh Creek', 'Loxton', 'Millicent', 'Mount Gambier', 'Murray Bridge', 'Naracoorte', 'Oodnadatta', 'Port Adelaide Enfield', 'Port Augusta', 'Port Lincoln', 'Port Pirie', 'Renmark', 'Victor Harbor', 'Whyalla'], 'Tasmania': ['Beaconsfield', 'Bell Bay', 'Burnie', 'Devonport', 'Hobart', 'Kingston', 'Launceston', 'New Norfolk', 'Queenstown', 'Richmond', 'Rosebery', 'Smithton', 'Stanley', 'Ulverstone', 'Wynyard'], 'Victoria': ['Wodonga', 'Mooroopna', 'Bright', 'Ararat', 'Bacchus Marsh', 'Bairnsdale', 'Ballarat', 'Beechworth', 'Benalla', 'Bendigo', 'Castlemaine', 'Colac', 'Echuca', 'Geelong', 'Hamilton', 'Healesville', 'Horsham', 'Kerang', 'Kyabram', 'Kyneton', 'Lakes Entrance', 'Maryborough', 'Melbourne', 'Mildura', 'Moe', 'Morwell', 'Port Fairy', 'Portland', 'Sale', 'Sea Lake', 'Seymour', 'Shepparton', 'Sunbury', 'Swan Hill', 'Traralgon', 'Yarrawonga', 'Wangaratta', 'Warragul', 'Werribee', 'Wonthaggi'], 'Western Australia': ['Broome', 'Bunbury', 'Busselton', 'Coolgardie', 'Dampier', 'Derby', 'Fremantle', 'Geraldton', 'Kalgoorlie', 'Kambalda', 'Katanning', 'Kwinana', 'Mandurah', 'Meekatharra', 'Mount Barker', 'Narrogin',
    'Newman', 'Northam', 'Perth', 'Perth (WA)', 'Port Hedland', 'Tom Price', 'Wyndham']}

try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepError:
    print('Error! Failed to get request token.')

def save_to_json(tweet):
    with open('data_5_20/australia_5_20_1.json', 'a') as json_file:
        json_str = json.dumps(tweet)
        json_file.write(json_str + "\n")

def save_to_db(tweet):
    db.update([tweet])

def process_tweet_data(data_json):
    try:
        print('----------------START PROCESS TWEET DATA------------:' + str(datetime.now()) + ' id: ' + data_json['id_str'])
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
        blob = TextBlob(tweet["text"])
        if blob.sentiment[0] >= 0:
            tweet["sentiment"] = "positive"
        else:
            tweet["sentiment"] = "negative"
        if data_json["geo"] is not None:
            tweet["geo"] = data_json["geo"]["coordinates"]
        else:
            tweet["geo"] = data_json["geo"]
        place["country"] = data_json["place"]["country"]
        place["full_name"] = data_json["place"]["full_name"]

        name_split = place["full_name"].split(", ")
        if len(name_split) == 1:
            if name_split[0] == "Australia":
                place["state"] = None
                place["city"] = None
            elif name_split[0] in AUSTRALIA_CITY.keys():
                place["state"] = name_split[0]
                place["city"] = None
            elif name_split[0] not in AUSTRALIA_CITY.keys():
                true_name = self.get_keys(AUSTRALIA_CITY, name_split[0])
                if true_name:
                    place["state"] = true_name
                    place["city"] = name_split[0]
                else:
                    place["state"] = None
                    place["city"] = name_split[0]
        elif len(name_split) == 2:
            state = place["full_name"].split(", ")[1]
            city = place["full_name"].split(", ")[0]
            if state == "Australia":
                place["state"] = city
                place["city"] = None
            elif state not in AUSTRALIA_CITY.keys():
                true_state = self.get_keys(AUSTRALIA_CITY,state)
                if true_state:
                    place["state"] = true_state
                    place["city"] = state
                else:
                    place["state"] = None
                    place["city"] = state
            else:
                place["state"] = state
                place["city"] = city
        else:
            place["state"] = None
            place["city"] = None

        place["coordinates"] = data_json["place"]["bounding_box"]["coordinates"]
        tweet["place"] = place
        print(tweet)
        save_to_json(tweet)
        save_to_db(tweet)
        print('----------------END PROCESS TWEET DATA------------:' + str(datetime.now()) + ' id: ' + data_json['id_str'])

    except BaseException as e:
        print('-----------------------GET EXCEPTION--------------------------' + str(datetime.now()) + ' id: ' + data_json['id_str'])
        print('failed on_status,', str(e))
        print(e)

class listener(StreamListener):

    def __init__(self):
        super().__init__()
        self.limit = 20000

    def get_keys(self, d, value):
        for k, v in d.items():
            if value in v:
                return k

    def on_data(self, data):
        data_json = json.loads(data)
        if (data_json['place'] is not None) and ("retweeted_status" not in data_json.keys()) and ("quoted_status" not in data_json.keys()) and (data_json["lang"] == "en") and (data_json["in_reply_to_status_id"] is None) and (data_json["place"]["country"] == "Australia"):
            try:
                process_tweet_data_thread = threading.Thread(target=process_tweet_data, args=(data_json, ))
                process_tweet_data_thread.start()
            except:
                print ("Error: unable to start thread")

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        # returning False in on_data disconnects the stream
        if status_code == 420:
            print('get a 420 code from twitter')
            print('-------------------sleep 90 seconds to reconnect------------------------')
            twitterStream.disconnect()
            time.sleep(90)
            twitterStream.filter(locations=AUSTRALIA, is_async=True)
            return True

twitterStream = Stream(auth=auth, listener=listener())
twitterStream.disconnect()

while True:
    try:
        twitterStream.filter(locations=AUSTRALIA, is_async=True)
    except (ProtocolError, AttributeError):
        print('------------------get ProtocolError or AttrbuteError------continue the stream-------')
        twitterStream.disconnect()
        time.sleep(90)
        continue
