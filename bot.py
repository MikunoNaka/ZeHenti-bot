import discord
import random
# import os  # why
# from hentai import hentai
# from dotenv import load_dotenv

# z!info
INFO_MESSAGE = "Discord bot created by Vidhu Kant Sharma"

greetings = ["Greetings", "Hello", "Hey", "Yahallo", "Namaskar", "Konnichiwa", "Yo"]



# load_dotenv()
# TOKEN = 








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
    
    if message.content[0:6] == 'z!say ':
        response = message.content[5:]
        await message.channel.send(response)
        
    
    if message.content == 'z!info':
        response = INFO_MESSAGE
        await message.channel.send(response)



client.run(TOKEN)
