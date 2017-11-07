import discord
from discord.ext import commands
import asyncio
import random

client = discord.Client()

description = "A bot for guessing numbers."

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'what')
    if message.content.startswith('start'):
        await client.send_message(message.channel, 'Beginning program. ' )
        y = 0
        z = 100000
        state = True
        while(state == True):
            await client.send_message(message.channel, 'g!start' )
            number = random.randint(y, z)
            await client.send_message(message.channel, 'g!guess ' + str(number))
            await client.send_message(message.channel, 'g!stop' )
            await asyncio.sleep(2)

client.run('user', 'pass')
