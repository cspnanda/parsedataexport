#!/usr/bin/env python

## Script to push a Dump of Parse JSON into a Custom MongoDB
## C S P Nanda <cspnanda@gmail.com
## For Test and Dev. Use at your own risk


import os,sys,json
import os.path
from pymongo import MongoClient

#### PLEASE CHANGE THIS ####
dbName = 'testdb'
connectionURI = "mongodb://username:password@host1.mongolab.com:53745,host2.mongolab.com:53745/testdb?replicaSet=rs-replName&ssl=true"
#### PLEASE CHANGE THIS ####

def cli_progress_test(curVal, end_val, bar_length=20):
	if(curVal == end_val):
		sys.stdout.write("\n\n")
		sys.stdout.flush()
	else:
    		percent = float(curVal) / end_val
    		hashes = '#' * int(round(percent * bar_length))
    		spaces = ' ' * (bar_length - len(hashes))
    		sys.stdout.write("\rInsert Into Mongo: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    		sys.stdout.flush()

if(len(sys.argv) != 2):
	print "Correct Usage " + sys.argv[0] + " CLASSNAME.json"
	sys.exit(-1)

if not os.path.isfile(sys.argv[1]):
	print "CLASS JSON File " + sys.argv[1] + " could not be opened"
	sys.exit(-1)

filename = sys.argv[1]
collection = filename.replace('.json','')
client = MongoClient(connectionURI)
db = client[dbname]
collection = db[collection]
with open(filename) as data_file:    
    data = json.load(data_file)
    if data:
        record = data['results'][0]
        keys = record.keys()
        if len(keys)>0:
	    print "Your Table View"
            print '{'
            for i in range(0,len(keys)):
		if i < len(keys)-1:
                    print '"'+keys[i]+'"'+':'+'"'+keys[i]+'"'+","
		else:
                    print '"'+keys[i]+'"'+':'+'"'+keys[i]+'"'
            print '}'
count = 1
for record in data['results']:
        findResult = None
        findResult = collection.find_one({'objectId':record['objectId']})
	if findResult != None:
	    collection.update({"_id":findResult['_id']},record)
        else:
	    collection.insert_one(record)
        cli_progress_test(count,len(data['results']))
	count = count + 1
