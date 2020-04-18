import pymongo
import os

def getABug(name, db):
    """
    give name get fish
    """
    print(name, db)
    bug = db.bugs.find_one({'name': name})
    print(bug)
    return bug
