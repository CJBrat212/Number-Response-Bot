import logging

logging.basicConfig(level=logging.INFO)
import asyncio
import discord
from discord.ext import commands
import random

description = "A bot for guessing numbers."

client = discord.Client()
client.login('token')
client.token = "###"

bot = commands.Bot(command_prefix='g!', description=description)

@client.event
async def on_ready():
    print('logged in ')

bot.run('token')
