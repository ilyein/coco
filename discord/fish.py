import pymongo
import os

def getAFish(name, db):
    """
    give name get fish
    """
    print(name, db)
    fish = db.fish.find_one({'name': name})
    return fish
