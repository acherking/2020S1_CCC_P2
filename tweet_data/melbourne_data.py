import ssl
import json
import time
import tweepy
import threading
import couchdb
import certifi
import numpy as np
import geopy.geocoders
from datetime import datetime
from textblob import TextBlob
from geopy.geocoders import Nominatim
from tweepy import StreamListener, Stream
from urllib3.exceptions import ProtocolError

server = couchdb.Server('http://admin:123456@172.26.131.241:5984/')
db = server.create('melbourne_5_20_3')

#server = couchdb.Server('http://admin:admin@127.0.0.1:5984/')
#db = server.create('test-melbourne_5_20')

consumer_key = 'Twd11SLSUOhAvpmXq94bTUTtA'
consumer_secret = 'lVfoW9DHTnWPMp8h0CxJbMn0AzNf9J84gl5o5iQMfis6hGJG1r'

access_token = '1249239316515016704-k5Zkh6S1aYULx4MupRbPY45YABO4nH'
access_token_secret = 'LdQxM8DcdPS6QcsSmoRcUQmo8nWxs9B37VrpNFKY6pbLs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

MELBOURNE = [144.30, -38.30, 145.50, -37.30]
AUSTRALIA = [112.35, -43.56, 154.41, -10.16]
MELBOURNE_SUBURB = ['Abbotsford', 'Aberfeldie', 'Airport West', 'Albanvale', 'Albert Park', 'Albion', 'Alphington', 'Altona', 'Altona Meadows', 'Altona North', 'Ardeer', 'Armadale', 'Armadale North', 'Arthurs Creek', 'Arthurs Seat', 'Ascot Vale', 'Ashburton', 'Ashwood', 'Aspendale', 'Aspendale Gardens', 'Attwood', 'Avondale Heights', 'Avonsleigh', 'Balaclava', 'Balnarring', 'Balwyn', 'Balwyn North', 'Bangholme', 'Banyule', 'Baxter', 'Bayswater', 'Bayswater North', 'Beaconsfield', 'Beaconsfield Upper', 'Beaumaris', 'Bedford Road', 'Belgrave', 'Belvedere Park', 'Bend Of Islands', 'Bennettswood', 'Bentleigh', 'Bentleigh East', 'Berwick', 'Bittern', 'Black Rock', 'Blackburn', 'Blackburn North', 'Blackburn South', 'Blairgowrie', 'Bonbeach', 'Boronia', 'Box Hill', 'Box Hill North', 'Box Hill South', 'Braeside', 'Braybrook', 'Brentford Square', 'Briar Hill', 'Brighton', 'Brighton East', 'Brighton Road', 'Broadmeadows', 'Brooklyn', 'Brunswick', 'Brunswick East', 'Brunswick West', 'Bulla', 'Bulleen', 'Bundoora', 'Burnley', 'Burnside', 'Burwood', 'Burwood East', 'Burwood Heights', 'Cairnlea', 'Camberwell', 'Camberwell East', 'Camberwell North', 'Camberwell South', 'Camberwell West', 'Campbellfield', 'Cannons Creek', 'Canterbury', 'Carlton', 'Carlton North', 'Carlton South', 'Carnegie', 'Caroline Springs', 'Carrum', 'Carrum Downs', 'Caulfield', 'Caulfield East', 'Caulfield Junction', 'Caulfield North', 'Caulfield South', 'Central Park', 'Chadstone', 'Chelsea', 'Chelsea Heights', 'Cheltenham', 'Cheltenham East', 'Chirnside Park', 'Christmas Hills', 'Clarinda', 'Clayton', 'Clayton South', 'Clematis', 'Clifton Hill', 'Coatesville', 'Coburg', 'Coburg North', 'Cockatoo', 'Coldstream', 'Collingwood', 'Collins Street East', 'Collins Street West', 'Coolaroo', 'Cottles Bridge', 'Craigieburn', 'Cranbourne', 'Cranbourne North', 'Cranbourne South', 'Cremorne', 'Crib Point', 'Cromer', 'Croydon', 'Croydon Hills', 'Croydon North', 'Croydon South', 'Dallas', 'Dandenong', 'Dandenong South', 'Dandenong South', 'Darling', 'Deer Park', 'Deer Park East', 'Delahey', 'Dendy', 'Derrimut', 'Devon Meadows', 'Diamond Creek', 'Diggers Rest', 'Dingley Village', 'Dixons Creek', 'Docklands', 'Doncaster', 'Doncaster East', 'Doncaster Heights', 'Donnybrook', 'Donvale', 'Doveton', 'Dromana', 'Eaglemont', 'East', 'East', 'Edithvale', 'Elsternwick', 'Eltham', 'Eltham North', 'Elwood', 'Emerald', 'Endeavour Hills', 'Epping', 'Epping Dc', 'Essendon', 'Essendon North', 'Essendon West', 'Fairfield', 'Fawkner', 'Ferntree Gully', 'Ferny Creek', 'Fingal', 'Fitzroy', 'Fitzroy North', 'Five Ways', 'Flemington', 'Flinders', 'Flinders Lane', 'Footscray', 'Forest Hill', 'Fountain Gate', 'Frankston', 'Frankston North', 'Garden City', 'Gardenvale', 'Gladstone Park', 'Glen Huntly', 'Glen Iris', 'Glen Waverley', 'Glenroy', 'Gowanbrae', 'Greensborough', 'Greenvale', 'Gruyere', 'Guys Hill', 'Hadfield', 'Hallam', 'Hampton', 'Hampton East', 'Hampton North', 'Hampton Park', 'Harkaway', 'Hastings', 'Hawksburn', 'Hawthorn', 'Hawthorn East', 'Healesville', 'Heatherton', 'Heathmont', 'Heidelberg', 'Heidelberg Heights', 'Heidelberg Rgh', 'Heidelberg West', 'Highett', 'Highpoint City', 'Hillside', 'Hmas Cerberus', 'Hoddles Creek', 'Holmesglen', 'Hopetoun Gardens', 'Hoppers Crossing', 'Hotham Hill', 'Houston', 'Hughesdale', 'Huntingdale', 'Hurstbridge', 'Ivanhoe', 'Ivanhoe East', 'Jacana', 'Kalkallo', 'Kallista', 'Kalorama', 'Kangaroo Ground', 'Karingal', 'Kealba', 'Keilor', 'Keilor Downs', 'Keilor East', 'Keilor North', 'Keilor Park', 'Kensington', 'Keon Park', 'Kerrimuir', 'Kew', 'Kew East', 'Keysborough', 'Kilsyth', 'Kilsyth South', 'Kings Park', 'Kingsbury', 'Kingsville', 'Knox City Centre', 'Knoxfield', 'Kooyong', 'Kunyung', 'Kurunjang', 'Laburnum', 'Lalor', 'Langwarrin', 'Launching Place', 'Laverton', 'Laverton North', 'Law Courts', 'Lilydale', 'Lower Plenty', 'Lynbrook', 'Lyndhurst', 'Lysterfield', 'Macclesfield', 'Macleod', 'Maidstone', 'Main Ridge', 'Malvern', 'Malvern East', 'Maribyrnong', 'Mccrae', 'Mckinnon', 'Meadow Heights', '', ' Airport', ' University', 'Melton', 'Mentone', 'Menzies Creek', 'Merlynston', 'Merricks', 'Merricks Beach', 'Merricks North', 'Mickleham', 'Middle Camberwell', 'Middle Park', 'Mill Park', 'Mitcham', 'Monbulk', 'Mont Albert', 'Mont Albert North', 'Montmorency', 'Montrose', 'Moonee Ponds', 'Moorabbin', 'Moorabbin Airport', 'Moorabbin East', 'Moorooduc', 'Mooroolbark', 'Mordialloc', 'Moreland', 'Mornington', 'Mount Cottrell', 'Mount Dandenong', 'Mount Eliza', 'Mount Evelyn', 'Mount Martha', 'Mount Waverley', 'Mountain Gate', 'Mulgrave', 'Murrumbeena', 'Narre Warren', 'Narre Warren East', 'Narre Warren North', 'Newport', 'Niddrie', 'Noble Park', 'Noble Park North', 'North', 'North Road', 'North Warrandyte', 'Northcote', 'Northland Centre', 'Notting Hill', 'Nunawading', 'Nunawading Bc', 'Nutfield', 'Oak Park', 'Oaklands Junction', 'Oakleigh', 'Oakleigh East', 'Oakleigh South', 'Officer', 'Olinda', 'Ormond', 'Pakenham', 'Pakenham Upper', 'Park Orchards', 'Parkdale', 'Parkville', 'Pascoe Vale', 'Pascoe Vale South', 'Patterson Lakes', 'Pearcedale', 'Pines Forest', 'Plenty', 'Point Cook', 'Port', 'Portsea', 'Prahran', 'Preston', 'Preston South', 'Rangeview', 'Red Hill', 'Red Hill South', 'Regent West', 'Research', 'Reservoir', 'Richmond', 'Ringwood', 'Ringwood East', 'Ringwood North', 'Ripponlea', 'Robinson', 'Rockbank', 'Rosanna', 'Rosebud', 'Rosebud West', 'Rowville', 'Roxburgh Park', 'Royal  Hospital', 'Rye', 'Safety Beach', 'Saint Helena', 'Sandown Village', 'Sandringham', 'Sassafras', 'Sassafras Gully', 'Scoresby', 'Scoresby Bc', 'Seabrook', 'Seaford', 'Seaholme', 'Seddon', 'Seddon West', 'Selby', 'Seville', 'Sherbrooke', 'Shoreham', 'Silvan', 'Skye', 'Somers', 'Somerton', 'Somerville', 'Sorrento', 'South Kingsville', 'South', 'South  Dc', 'South Morang', 'South Yarra', 'Southbank', 'Southland Centre', 'Spotswood', 'Springvale', 'Springvale South', 'St Albans', 'St Andrews Beach', 'St Kilda', 'St Kilda East', 'St Kilda Road', 'St Kilda Road Central', 'St Kilda South', 'St Kilda West', 'Steels Creek', 'Strathewen', 'Strathmore', 'Strathmore Heights', 'Studfield', 'Sunbury', 'Sunshine', 'Surrey Hills', 'Sydenham', 'Syndal', 'Tarneit', 'Taylors Lakes', 'Tecoma', 'Templestowe', 'Templestowe Lower', 'The Basin', 'The Patch', 'Thomastown', 'Thornbury', 'Toolangi', 'Toolern Vale', 'Toorak', 'Tootgarook', 'Tottenham', 'Travancore', 'Truganina', 'Tuerong', 'Tullamarine', 'Tunstall Square Po', 'Tyabb', 'University Of', 'Upper Ferntree Gully', 'Upwey', 'Vermont', 'Vermont South', 'Viewbank', 'Wandin North', 'Wantirna', 'Wantirna South', 'Warrandyte', 'Warrandyte South', 'Warranwood', 'Waterways', 'Watsonia', 'Watsons Creek', 'Wattle Glen', 'Wattle Park', 'Werribee', 'West Footscray', 'West', 'Westmeadows', 'Wheelers Hill', 'Williamstown', 'Windsor', 'Wishart', 'Wonga Park', 'Woori Yallock', 'World Trade Centre', 'World Trade Centre', 'Wyndham Vale', 'Yallambie', 'Yarra Glen', 'Yarrambat', 'Yarraville', 'Yarraville West', 'Yellingbo', 'Yuroke']

try:
    redirect_url = auth.get_authorization_url()
    print(redirect_url)
except tweepy.TweepError:
    print('Error! Failed to get request token.')

def save_to_json(tweet):
    with open('data_5_20/melbourne_5_20_3.json', 'a') as json_file:
        json_str = json.dumps(tweet)
        json_file.write(json_str + "\n")

def save_to_db(tweet):
    db.update([tweet])

def convert_to_sub(coordinate):
    coordinate_np = (np.sum([coordinate[0], coordinate[1], coordinate[2], coordinate[3]], axis=0)) / 4
    coordinate_list = coordinate_np.tolist()
    coordinates = str(coordinate_list[1]) + ", " + str(coordinate_list[0])
    nominatim = Nominatim(user_agent="ccc_geo")
    locations = nominatim.reverse(coordinates)
    locations = str(locations).split(", ")
    for i in locations:
        if i in MELBOURNE_SUBURB:
            location = i
            break
        else:
            location = locations[1]
    return location

def process_tweet_data(data_json):
    try:
        place = dict()
        place["full_name"] = data_json["place"]["full_name"]
        name_split = place["full_name"].split(", ")
        if len(name_split) == 2:
            state = place["full_name"].split(", ")[1]
            city = place["full_name"].split(", ")[0]
            if state == "Victoria":
                if city == "Melbourne":
                    print('----------------START PROCESS TWEET DATA------------:' + str(datetime.now()) + ' id: ' +
                          data_json['id_str'])
                    place["state"] = state
                    place["city"] = city
                else:
                    return True
            elif state == "Melbourne":
                print(
                    '----------------START PROCESS TWEET DATA------------:' + str(datetime.now()) + ' id: ' + data_json[
                        'id_str'])
                place["state"] = None
                place["city"] = state
            else:
                return True
            tweet = dict()
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
            place["coordinates"] = data_json["place"]["bounding_box"]["coordinates"]
            suburb = convert_to_sub(place["coordinates"][0])
            place["suburb"] = suburb
            if ((abs(place["coordinates"][0][0][0] - place["coordinates"][0][2][0])) > 0.5) or (
                    (abs(place["coordinates"][0][0][1] - place["coordinates"][0][1][1])) > 0.5):
                place["suburb_is_ignore"] = True
            elif suburb not in MELBOURNE_SUBURB:
                place["suburb_is_ignore"] = True
            else:
                place["suburb_is_ignore"] = False
            tweet["place"] = place
        else:
            return True
        print(tweet)
        save_to_json(tweet)
        save_to_db(tweet)
        print('----------------END PROCESS TWEET DATA------------:' + str(datetime.now()) + ' id: ' + data_json['id_str'])
    except BaseException as e:
        print('----------------GET EXCEPTION------------:' + str(datetime.now()) + ' id: ' + data_json['id_str'])
        print(e)

class listener(StreamListener):

    def __init__(self):
        super().__init__()
        default_context = ssl.create_default_context(cafile=certifi.where())
        geopy.geocoders.options.default_ssl_context = default_context
        self.limit = 20000


    def on_data(self, data):
        data_json = json.loads(data)
        if (data_json['place'] is not None) and ("retweeted_status" not in data_json.keys()) and ("quoted_status" not in data_json.keys()) and (data_json["lang"] == "en")\
                and (data_json["in_reply_to_status_id"] is None) and (data_json["place"]["country"] == "Australia"):
            try:
                process_tweet_data_thread = threading.Thread(target=process_tweet_data, args=(data_json, ))
                process_tweet_data_thread.start()
            except:
                print ("Error: unable to start thread")

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            print('get a 420 code from twitter')
            print('-------------------sleep 90 seconds to reconnect------------------------')
            twitterStream.disconnect()
            time.sleep(90)
            twitterStream.filter(locations=MELBOURNE, is_async=True)
            return True

twitterStream = Stream(auth=auth, listener=listener())
twitterStream.disconnect()

while True:
    try:
        twitterStream.filter(locations=MELBOURNE, is_async=True)
    except (ProtocolError, AttributeError):
        print('------------------get ProtocolError or AttrbuteError------continue the stream-------')
        twitterStream.disconnect()
        time.sleep(90)
        continue


