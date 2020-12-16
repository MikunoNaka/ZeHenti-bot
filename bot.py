import discord
import os
from dotenv import load_dotenv
import random
import math
import henti as H  # the good stuff

greetings = ["Greetings.", "Hello.", "Hey!", "Yahallo!", "Namaskar,", "Konnichiwa,", "Yo!"]
def get_info():
    info_messages = [random.choice(greetings) + " I'm a Discord bot created by Vidhu Kant Sharma", "This bot is pog"]
    return random.choice(info_messages)

bad_words = ['fuck', 'shit', 'bitch', 'cunt', 'sex']#, '', '', '', '', '', '', '', '', '', '', '', '')

# z!help
def show_help():
    help = open('help_message.txt', 'r')
    help_message = help.read()
    return help_message


CALL = "z!"

HELP_MESSAGE = '```Every command should be prefixed with "' + CALL + '".\n\nsay      repeats your previous message\ninfo     displays info about the bot and the creator\nhelp     shows this message```'
















load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# frontend stuff
client = discord.Client()

# events
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game('Guess you are my little pogchamp'))



@client.event
async def on_message(message):
    # ignore if sent by itself
    if message.author == client.user:
        return
   
    # say something
    if message.content[0:len(CALL) + 4] == CALL + 'say ':
        response = message.content[5:] # users message with the command removed

        # check if the user said a bad word
        if response[1:] in bad_words: # for some reason the first character is always a space
            await message.channel.send('THIS IS A FAMILY FRIENDLY DISCORD SERVER')
            await message.channel.send('NO ONE WILL FUCKING CURSE')
        else:
            await message.channel.send(response)

    # send info message 
    if message.content == CALL + 'info':
        response = get_info()
        await message.channel.send(response)
 
    if message.content == CALL + 'repo':
        response = 'My source code: https://github.com/MikunoNaka/ZeHenti-bot.git'
        await message.channel.send(response)
    
    # send help message
    if message.content == CALL + 'help':
        response = show_help()
        await message.channel.send(response)
    
    # cultured stuff
    if message.content.split()[0] == CALL + 'find':  # find title of henti 
        sauce = (''.join(message.content.split()[1:])) 
        response = H.find_title(sauce)
        await message.channel.send(response)


client.run(TOKEN)
