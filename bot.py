import discord
import os
from dotenv import load_dotenv
import random
# from hentai import hentai

greetings = ["Greetings.", "Hello.", "Hey!", "Yahallo!", "Namaskar,", "Konnichiwa,", "Yo!"]
def get_info():
    info_messages = [random.choice(greetings) + " I'm a Discord bot created by Vidhu Kant Sharma", "This bot is pog"]
    return random.choice(info_messages)

CALL = "z!"
HELP_MESSAGE = '```Every command should be prefixed with "' + CALL + '".\nsay      repeats your previous message\ninfo     displays info about the bot and the creator\nhelp     shows this message```'

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# frontend stuff
client = discord.Client()

# events
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content[0:len(CALL) + 4] == CALL + 'say ':
        response = message.content[5:]
        await message.channel.send(response)
        
    if message.content == CALL + 'info':
        response = get_info()
        await message.channel.send(response)

    if message.content == CALL + 'help':
        response = HELP_MESSAGE
        await message.channel.send(response)


client.run(TOKEN)
