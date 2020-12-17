import os
import random

from dotenv import load_dotenv
from discord.ext import commands

from henti import Numbers as n

load_dotenv()  # load .env file
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='z!')  # initialise the bot




# get title of henti
@bot.command(name='info', help='Get the title of doujin using the holy numbers')
async def getInfo(ctx, sauce):
    r = n(sauce).title()
    await ctx.send(r)

# short for the same
@bot.command(name='i', help='short fot z!title')
async def getInfo(ctx, sauce):
    r = n(sauce).title()
    await ctx.send(r)


# @bot.command(name='', help='')
# async def 




bot.run(TOKEN)

