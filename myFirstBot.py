import discord  # Import the relevent discord Framework
import logging  # Use Py's logging module to track errors
from discord.ext import commands
from classes.party import Party
import os
from dotenv import load_dotenv
load_dotenv()

BOT_KEY = os.getenv("BOT_KEY")

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

# This command will create a party oject with the caller as the owner
@bot.command()
async def cParty(ctx, pSize:int ,*, name:str):
    await ctx.send("Creating party of: size = " + str(pSize) + ",\n Name = " + name + ",\nOwner = " + ctx.author)
    partyList.append(Party(pSize, name, ctx.author))
    author = ctx.message.author
    await client.create_role(author.server, name="party:"+name, color=discord.Colour.from_rgb(78, 255, 33))

@bot.command()
async def listParty(ctx, *, searchName:str):
    rolesList = ctx.author.roles
    await ctx.send(rolesList)
    partyList = []
    for role in rolesList:
        if "party:" in role[:6]:
            partyList.append(role[6:])

    # if len(partyList):
    #     await ctx.send(("You are currently part of no parties. \n"
    #         "To create a party use: ?cParty [party Size] [Name of Party]\n"
    #         "To list all recruiting parties use: ?findParties"))
    # elif(searchName != ""):
    #     if (searchName in partyList):
    #         discord.role

bot.run(BOT_KEY)
