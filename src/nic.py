import asyncio
import discord
from dotenv import load_dotenv
import os
import random

from NicNames import nicNames
from NicQuotes import nicQuotes
from NicWatches import nicWatches

client = discord.Client()

@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    message_lower = (message.content).lower()

    if message.author == client.user:
        return

    elif any(x in message_lower for x in nicNames):
        print('I found a message for me: {}'.format(message_lower))
        answer = random.choice(nicQuotes)
        await message.channel.send(answer)
        
    elif message.content == 'raise-exception':
        raise discord.DiscordException

async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        movie = random.choice(nicWatches)
        activity = discord.Activity(type = discord.ActivityType.watching, name = movie)
        await client.change_presence(status = discord.Status.online, activity=activity)
        print("I'm watching a different movie now: {}".format(movie))
        await asyncio.sleep(14400) #4 hours
        
client.loop.create_task(my_background_task())

load_dotenv()
DISCORD_API = os.getenv('DISCORD_API')
client.run(DISCORD_API)