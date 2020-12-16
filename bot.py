import os

from dotenv import load_dotenv
from discord.ext import commands

import henti as H

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='z!')

# get title of henti
@bot.command(name='title', help='Get the title of doujin using the holy numbers')
async def nine_nine(ctx, sauce):
    r =  H.get_title(sauce)
    await ctx.send(r)

bot.run(TOKEN)

