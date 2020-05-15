from couchdb import *
import json
"""
server = Server('http://admin:123456@172.26.132.113:5984/')
server.delete('test3')

db = server.create('test3')

#test_data_file = open("/home/ubuntu/test.json")
#docs = json.loads(test_data_file.read())
#db.update(docs)

db['johndoe'] = dict(type='Person', name='John Doe')
db['maryjane'] = dict(type='Person', name='Mary Jane')
db['gotham'] = dict(type='City', name='Gotham City')


#mango = {'selector': {'type': 'Person'}, 'fields': ['name']}
def readcouchdb():
	result = []
	for a in db:
		result.append(db[a].get('name'))
	return result"""