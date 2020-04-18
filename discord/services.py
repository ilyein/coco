import pymongo
from pymongo import collation
import os
import discord
"""
More of a playbook to init collections..shouldn't have to do this but just in case.
"""



def connections():
    mongoclient = pymongo.MongoClient("redacted for security conecerns TODO add to env on startup")
    discordclient = discord.Client()
    return discordclient, mongoclient



if __name__ == "__main__":
    client, garbage = connections()
    cocodb = garbage.cocodb




    #cocodb.create_collection('fish', collation=collation.Collation(locale='en_US', strength = 2))
    cocodb.create_collection('bugs', collation=collation.Collation(locale='en_US', strength = 2))


    #cocodb.create_collection('villagers', collation=Collation(locale='en_US', strength = 2))

    cocodb.fish.create_index([("name", pymongo.ASCENDING),("hemisphere", pymongo.ASCENDING)], unique = True)
    cocodb.bugs.create_index([("name", pymongo.ASCENDING),("hemisphere", pymongo.ASCENDING)], unique = True)


