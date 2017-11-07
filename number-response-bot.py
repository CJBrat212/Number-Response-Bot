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
        await client.send_message(message.channel, 'g!start' )
        y = 0
        z = 100000
        state = True
        while(state == True):
            hl = True
            number = random.randint(y, z)
            await client.send_message(message.channel, 'g!guess ' + str(number))
            async def on_message(message):
                if message.content.contains('**Higher!**'):
                    y += 1000
                    hl = True
                if message.content.startswith('**Lower!**'):
                    z -= 1000
                    hl = False
                if message.content.startswith('!Stop'):
                    state = False
            await client.send_message(message.channel, str(y) + ' and ' + str(z) + ' and ' + str(hl))
        await client.send_message(message.channel, 'g!stop' )

client.run('user', 'password')
