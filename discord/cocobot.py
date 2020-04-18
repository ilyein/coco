import discord
import pymongo
from services import connections
from fish import getAFish
from bugs import getABug

discord_client, mongo_client = connections()

@discord_client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(discord_client))

@discord_client.event
async def on_message(message):
    if message.author == discord_client.user:
        return
    if message.content.startswith('!fish'):
        print(type(message.content))
        arg = message.content.split(' ', 1)[1]
        fish = getAFish(arg, mongo_client.cocodb)
        await message.channel.send(fish)
    elif message.content.startswith('!bug'):
        print(type(message.content))
        arg = message.content.split(' ', 1)[1]
        bug = getABug(arg, mongo_client.cocodb)
        await message.channel.send(bug)


discord_client.run('NzAxMTAzNTczMTMxNDYwNjUw.XpsoNQ.et8nu0D1Btp1d9yJcL_xwcxTHAs')