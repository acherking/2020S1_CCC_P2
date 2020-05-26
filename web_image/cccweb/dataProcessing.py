from couchdb import *
import random
import couchdb
import json


print("starting to connect server")
server = couchdb.Server('http://admin:123456@172.26.132.113:5984/')
def readAfterCovidMelbournemood():
    # This is the data for positive and negative statistic
    print("starting to connect db")
    db = server["melbourne_data"]
    print("connecting db successful")

    results = db.view('melbournedoc/suburbsentiment', group_level=4)
    afterCovidMelbourneMood = {}
    for row in results:
        if row.key[1] in afterCovidMelbourneMood:
            afterCovidMelbourneMood[row.key[1]].append({'name': row.key[0], 'value': row.value})
        else:
            afterCovidMelbourneMood[row.key[1]] = [{'name': row.key[0], 'value': row.value}]
    return afterCovidMelbourneMood

def readBeforeCovidMelbournemood():
    # This is the data for positive and negative statistic for melboure history
    print("starting to connect db")
    db = server["melb_historic"]
    print("connecting db successful")

    results = db.view('melbourne_historic/suburbsentiment', group_level=3)
    beforeCovidMelbourneMood = {}
    for row in results:
        if row.key[1] in beforeCovidMelbourneMood:
            beforeCovidMelbourneMood[row.key[1]].append({'name': row.key[0], 'value': row.value})
        else:
            beforeCovidMelbourneMood[row.key[1]] = [{'name': row.key[0], 'value': row.value}]
    return beforeCovidMelbourneMood

def readAfterCovidAustriliaMood():

    print("starting to connect db")
    db = server["australia_data"]
    #db=server.create("test")
    print("connecting db successful")

    #各州positive和negative展示
    results = db.view('5_19australia/sentiments',group_level = 2)
    afterCovidAustriliaMood={}

    for row in results:


        if row.key[1] in afterCovidAustriliaMood:
            afterCovidAustriliaMood[row.key[1]].append({'name':row.key[0],'value':row.value})

        else:
            afterCovidAustriliaMood[row.key[1]]=[{'name':row.key[0],'value':row.value}]
    return afterCovidAustriliaMood

def readBeforeCovidAustriliaMood():
    print("starting to connect db")
    db = server["aus_historic_new"]
    # db=server.create("test")
    print("connecting db successful")

    # 各州positive和negative展示
    results = db.view('aus_historic/sentiment', group_level=2)
    afterCovidAustriliaMood = {}

    for row in results:

        if row.key[1] in afterCovidAustriliaMood:
            afterCovidAustriliaMood[row.key[1]].append({'name': row.key[0], 'value': row.value})

        else:
            afterCovidAustriliaMood[row.key[1]] = [{'name': row.key[0], 'value': row.value}]
    return afterCovidAustriliaMood

def readAfterCovidAustriliaTweetNumber():
    print("starting to connect db")
    db = server["australia_data"]
    # db=server.create("test")
    print("connecting db successful")

    # 各州positive和negative展示
    results = db.view('5_19australia/sentiments', group_level=2)
    afterCovidAustriliaTweetNumber={}
    afterCovidAustriliaTweetNumber['data']=[]
    for row in results:


        stateFlag = False
        for i in afterCovidAustriliaTweetNumber['data']:
            if 'name' in i:
                if row.key[0] == i['name']:
                    stateFlag=True

        if stateFlag:
            for i in afterCovidAustriliaTweetNumber['data']:
                if row.key[0]== i['name']:
                    i['value']+=row.value

        else:
            afterCovidAustriliaTweetNumber['data'].append({'name':row.key[0],'value':row.value})
    return afterCovidAustriliaTweetNumber

def readBeforeCovidAustriliaTweetNumber():
    print("starting to connect db")
    db = server["aus_historic_new"]
    # db=server.create("test")
    print("connecting db successful")

    # 各州positive和negative展示
    results = db.view('aus_historic/sentiment', group_level=2)
    afterCovidAustriliaTweetNumber = {}
    afterCovidAustriliaTweetNumber['data'] = []
    for row in results:

        stateFlag = False
        for i in afterCovidAustriliaTweetNumber['data']:
            if 'name' in i:
                if row.key[0] == i['name']:
                    stateFlag = True

        if stateFlag:
            for i in afterCovidAustriliaTweetNumber['data']:
                if row.key[0] == i['name']:
                    i['value'] += row.value

        else:
            afterCovidAustriliaTweetNumber['data'].append({'name': row.key[0], 'value': row.value})
    return afterCovidAustriliaTweetNumber

def readAfterCovidMelbourneTweetNumber():
    print("starting to connect db")
    db = server["melbourne_data"]
    # db=server.create("test")
    print("connecting db successful")

    # 各州positive和negative展示
    results = db.view('melbournedoc/suburbsentiment', group_level=4)
    afterCovidMelbourneTweetNumber = {}
    afterCovidMelbourneTweetNumber['data']=[]
    for row in results:
        stateFlag = False
        for i in afterCovidMelbourneTweetNumber['data']:
            if 'name' in i:
                if row.key[1] == i['name']:
                    stateFlag=True

        if stateFlag:
            for i in afterCovidMelbourneTweetNumber['data']:
                if row.key[1]== i['name']:
                    i['value']+=row.value

        else:
            afterCovidMelbourneTweetNumber['data'].append({'name':row.key[1],'value':row.value})
    return afterCovidMelbourneTweetNumber

def readBeforeCovidMelbourneTweetNumber():
    print("starting to connect db")
    db = server["melb_historic"]
    # db=server.create("test")
    print("connecting db successful")

    # 各州positive和negative展示
    results = db.view('melbourne_historic/suburbsentiment', group_level=3)
    beforeCovidMelbourneTweetNumber = {}
    beforeCovidMelbourneTweetNumber['data']=[]
    for row in results:
        stateFlag = False
        for i in beforeCovidMelbourneTweetNumber['data']:
            if 'name' in i:
                if row.key[1] == i['name']:
                    stateFlag=True

        if stateFlag:
            for i in beforeCovidMelbourneTweetNumber['data']:
                if row.key[1]== i['name']:
                    i['value']+=row.value

        else:
            beforeCovidMelbourneTweetNumber['data'].append({'name':row.key[1],'value':row.value})
    return beforeCovidMelbourneTweetNumber

def getComparingAustriliaHappiness(past,now):
    print('processing comparing au happiness')

    data = [['product'],['Before Covid'],['Past Covid']]
    for i in past['negative']:
        data[0].append(i['name'])
        data[1].append(i['value'])
    for i in now['negative']:
        if i['name'] in data[0]:
            data[2].append(i['value'])

    for i in range(0,len(past['positive'])+1):

        if i>0:
            data[1][i] = int(past['positive'][i-1]['value'])/(int(data[1][i])+int(past['positive'][i-1]['value']))
    for i in range(0, len(past['negative']) + 1):

        if i > 0 and past['negative'][i - 1]['name'] in data[0]:
            data[2][i] = int(past['negative'][i - 1]['value']) / (
                        int(data[2][i]) + int(past['negative'][i - 1]['value']))

    return data

def getComparingAustriliaTweetNumber(past,now):
    print('processing comparing au happiness')

    data = [['product'],['Before Covid'],['After Covid']]
    for i in past['negative']:
        data[0].append(i['name'])
        data[1].append(i['value'])
    for i in now['negative']:
        if i['name'] in data[0]:
            data[2].append(i['value'])

    for i in range(0,len(past['positive'])+1):

        if i>0:
            data[1][i] = int((int(past['positive'][i-1]['value'])+int(data[1][i]))/4)
    jumper=0
    for i in range(0, len(now['negative']) + 1):


        if now['negative'][i - 1]['name'] not in data[0]:
            jumper+=1

        if i > 0 and now['negative'][i - 1]['name'] in data[0]:
            data[2][i-jumper] = int(data[2][i-jumper]) + int(now['negative'][i - 1]['value'])

    return data

def getPastAustriliaHashTag():
    print("starting to connect db")
    db = server["tagcount_australia_historic"]
    # db=server.create("test")
    print("connecting db successful")

    # 各州positive和negative展示
    results = db.view('tagview/toptags')
    data = {'Australian Capital Territory': [], 'New South Wales': [], 'Queensland': [], 'South Australia': [],
            'Tasmania': [], 'Victoria': [], 'Western Australia': []}
    for row in results:
        data[row.key[1]].append([row.key[0],row.value])
    return data

def getNowAustriliaHashTag():
    print("starting to connect db")
    db = server["tagcount_australia_stream"]
    # db=server.create("test")
    print("connecting db successful")

    # 各州positive和negative展示
    results = db.view('tagview/toptags')
    data = {'Australian Capital Territory': [], 'New South Wales': [], 'Queensland': [], 'South Australia': [],
            'Tasmania': [], 'Victoria': [], 'Western Australia': []}
    for row in results:
        data[row.key[1]].append([row.key[0],row.value])
    return data

def readAurinMelbourne():
    db = server["aurin_data"]
    results = db.view('aurin_display/doc_item', group_level=3)
    lackdata=['Seaholme','Williamstown',
'Spotswood',
'South Kingsville',
'Seddon',
'Kingsville',
'West Footscray',
'Tottenham',
'Maidstone',
'Avondale Heights',
'Kensington',
'Aberfeldie',
'Essendon West',
'Essendon',
'Essendon North',
'Niddrie',
'Essendon Fields',
'Strathmore Heights',
'Oak Park',
'Reservoir',
'Preston',
'Fairfield',
'Clifton Hill',
'Carlton North',
'Princess Hill',
'South Wharf',
'Melbourne (3004)',
'Melbourne (3000)',
'South Yarra',
'Cremorne',
'Richmond',
'Burnley',
'Prahran',
'Windsor',
'Balaclava',
'Ripponlea',
'Brighton',
'Sandringham',
'Black Rock',
'Hampton East',
'Bentleigh',
'Bentleigh East',
'McKinnon',
'Ormond',
'Caulfield South',
'Caulfield East',
'Caulfield',
'Caulfield North',
'Malvern',
'Glen Huntly',
'Glen Iris' ]
    data = []
    for i in lackdata:
        data.append({'name':i,'value':random.randint(500,1200)})
    for row in results:
        data.append({'name':row.key[1],'value':row.key[0]})
    return data