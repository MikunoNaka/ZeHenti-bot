import os
import random

from dotenv import load_dotenv
from discord.ext import commands

from henti import Numbers

load_dotenv()  # load .env file
TOKEN = os.getenv('DISCORD_TOKEN')

PREFIXES = ['z!', '?']  # prefixes for the bot's commands
bot = commands.Bot(command_prefix=PREFIXES)  # initialise the bot with pre-defined prefixes




# get title of henti
@bot.command(name='info', help='Get the info about a doujin using the holy numbers')
async def getInfo(ctx, sauce):
    doujin = Numbers(sauce)
    r = doujin.title()
    await ctx.send(r)

# short for the same
@bot.command(name='i', help='short fot z!info')
async def getInfo(ctx, sauce):
    doujin = Numbers(sauce)
    r = doujin.info()
    await ctx.send(r)


# @bot.command(name='', help='')
# async def 




bot.run(TOKEN)

