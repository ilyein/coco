"""
Scraping bugs from wiki.

"""
import requests
from pymongo import MongoClient
import os
from bs4 import BeautifulSoup
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

def insertBugs(hemisphere, coll):
    bugs = coll
    BUG_URL = "https://animalcrossing.fandom.com/wiki/Bugs_(New_Horizons)"
    page = requests.get(BUG_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    if hemisphere == 'north':
        north = soup.find_all('table', class_='roundy')[2]
        rows = north.find_all('tr')
    else:
        south = soup.find_all('table', class_='roundy')[3]
        rows = south.find_all('tr')
    header = rows[2]
    for row in rows[3:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        bug = { 
            "name": cols[0],
            "price": cols[2],
            "location": cols[3],
            "time": cols[4],
            "months": monthAvailable(cols[5:]),
            "hemisphere": hemisphere
        }
        print('inserting bug:', bug['name'])
        bugs.insert_one(bug)
    print(hemisphere, 'bug inserted')


if __name__ == "__main__":
    client = MongoClient(os.environ['conn_key'])
    client.cocodb.bugs.delete_many({})
    insertBugs('north', client.cocodb.bugs)
    insertBugs('south', client.cocodb.bugs)