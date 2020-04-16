import pymongo
import os
"""
More of a playbook to init collections..shouldn't have to do this but just in case.
"""

client = pymongo.MongoClient(os.environ['conn_key'])
cocodb = client.cocodb
cocodb.create_collection('fish', collation=Collation(locale='en_US', strength = 2))
cocodb.create_collection('bugs', collation=Collation(locale='en_US', strength = 2))


cocodb.create_collection('villagers', collation=Collation(locale='en_US', strength = 2))

cocodb.fish.create_index([("name", pymongo.ASCENDING),("hemisphere", pymongo.ASCENDING)], unique = True)
cocodb.bugs.create_index([("name", pymongo.ASCENDING),("hemisphere", pymongo.ASCENDING)], unique = True)


