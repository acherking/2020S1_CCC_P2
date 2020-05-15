import json
import datetime
from .settings import jsonpath
path = jsonpath
#This is the function to count the number of hashtag
def counthashtag(hashtag,counter):

    try:
        if counter[hashtag] > 0:
            counter[hashtag] += 1
    except:
        counter[hashtag] = 1
    return counter

#This is the function to remove smallest item in top
def delminitop(top):
    min = 9999999
    min_key = ''
    for key in top:
        if top[key] < min:
            min_key = key
            min = top[key]
    del top[min_key]
    return top

#This is the function to count the top 10 frequency
def counttop(counter):
    top = {}
    mini_fre = 0
    for key in counter:

        if counter[key] > mini_fre and len(top) < 9:
            top[key] = counter[key]
        elif counter[key] > mini_fre and len(top) == 9:
            mini_fre = counter[key]
            top[key] = counter[key]
        else:
            mini_fre = counter[key]
            top = delminitop(top)

            top[key] = counter[key]
    return top

def processing(line,counter):
    json_info = json.loads(line)

    doc = json_info['doc']

    entities = doc['entities']

    hashtags = entities['hashtags']

    for tags in hashtags:
        hashtag = tags['text']
        hashtag = hashtag.lower()
        counthashtag(hashtag, counter)
    return counter

def ranktopcounter(counter):
    max = 0
    rankedcounter = {}
    max_hashtag = ''
    while len(counter) > 0:
        for hashtag in counter:
            if counter[hashtag] > max:
                max = counter[hashtag]
                max_hashtag = hashtag
        rankedcounter[max_hashtag] = max
        del counter[max_hashtag]
        max = 0
        max_hashtag = ''
    return rankedcounter

def showresult(counter):
    i = 1
    for hashtag in counter:
        print(i,'. #%s'% hashtag,',',counter[hashtag])
        i += 1

def processingdata():
    with open(path,'r', encoding='utf-8') as f:
        starttime = datetime.datetime.now()
        counter={}
        #print('processing...')
        for i,line in enumerate(f):
            #delete the last \n and ,
            line = line[:-2]

            if i>1 and i<4057524:
                processing(line,counter)

        endtime = datetime.datetime.now()
        time = (endtime-starttime)
        #print('len of counter 1: ', len(counter))
        top = counttop(counter)

        #showresult(ranktopcounter(top))

        #print('\n','The cost time is:',time )
        return top
