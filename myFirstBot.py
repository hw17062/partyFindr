import discord  # Import the relevent discord Framework
import logging  # Use Py's logging module to track errors
from discord.ext import commands
from classes.party import Party

prefix = "?"
bot = commands.Bot(command_prefix='?')

# This will store the list of Parties currently active
partyList = []

#   Here we want to track errors from discord and save them to an external file for furure viewing
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)  #   Set level to debug to see all errors
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#   next we will take serious errors and display them immidiatly to the command line
logging.basicConfig(level=logging.ERROR)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Base event, will say 'hello' to anyone that says it to them
@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command()
async def cParty(ctx, pSize:int ,*, name:str):
    await ctx.send("Creating party of: size = " + str(pSize) + ", Name = " + name + ",Owner = " + ctx.author)
    partyList.append(Party(pSize, name, ctx.author))


bot.run('NzE4MjE1NzQ5OTEwMzk2OTYw.XuFvNg.dr5iTG0idYopbIB4GsE6smc64us')
