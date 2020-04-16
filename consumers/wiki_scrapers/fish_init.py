import requests
import pymongo
from bs4 import BeautifulSoup
import os


def monthAvailable(x):
    """
    x:arr
    return
    """
    res = []
    months = {
        1: "Jan",
        2: 'Feb',
        3: 'Mar',
        4: 'Apr', 
        5: 'May', 
        6: 'Jun',
        7: 'Jul',
        8: 'Aug',
        9: 'Sep',
        10: 'Oct',
        11: 'Nov',
        12: 'Dec'
    }
    for i in range(0, len(x)):
        if x[i] == '-':
            pass
        else:
            res.append(months[i+1])
    return res


def insertFish(hemisphere, coll):
    fish = coll
    FISH_URL = "https://animalcrossing.fandom.com/wiki/Fish_(New_Horizons)"
    page = requests.get(FISH_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    if hemisphere == 'north':
        north = soup.find_all('table', class_='roundy')[1]
        rows = north.find_all('tr')
    else:
        south = soup.find_all('table', class_='roundy')[3]
        rows = south.find_all('tr')
    header = rows[1]
    for row in rows[2:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        one_fish = {
            "name": cols[0],
            "price": cols[2],
            "location": cols[3],
            "shadowsize": cols[4],
            "time": cols[5],
            "months": monthAvailable(cols[6:]),
            "hemisphere": hemisphere
        }
        #TODO logger
        print('inserting fish:', one_fish['name'])
        fish.insert_one(one_fish)
    print(hemisphere, 'fish inserted')


if __name__ == "__main__":
    client = pymongo.MongoClient(os.environ['conn_key'])
    db = client.cocodb
    fish = db.fish
    fish.delete_many({})
    insertFish('north', fish)
    insertFish('south', fish)