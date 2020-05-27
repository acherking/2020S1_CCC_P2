import couchdb

print("starting to connect server")
server = couchdb.Server('http://admin:123456@172.26.132.113:5984/')

print("starting to connect db")
db = server["aus_historic_new"]
print("connecting db successful")

server2 = couchdb.Server('http://admin:123456@172.26.132.113:5984')
db2 = server2.create("tagcount_australia_historic")

limit = 400 #user efined

results = db.view('aus_historic/hashtags',group_level = 2)
for a in results:
    if a.value > limit:
         db2.update([{"tagCity" : a.key, "count" : a.value}])
