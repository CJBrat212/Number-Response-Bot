import discord
from discord.ext import commands
import asyncio
import random

client = discord.Client()

description = "A bot for guessing numbers."

bot = commands.Bot(command_prefix='g!', description=description)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@bot.command()
async def ping():
    await bot.say('Pong! Hello!')

bot.run('token_here')
