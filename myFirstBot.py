import discord  # Import the relevent discord Framework
import logging  # Use Py's logging module to track errors
from discord.ext import commands
from classes.party import Party
import sys
import os
from dotenv import load_dotenv
load_dotenv()

BOT_KEY = os.getenv("BOT_KEY")

bot = commands.Bot(command_prefix='?')

# This will store the list of Parties currently active
# Key = Guild, Value = list of parties
partyList = {}

#   Here we want to track errors from discord and save them to an external file for furure viewing
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

# set handler for all messages to be stored in a file
handler = logging.FileHandler("discord.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#   next we will take serious errors and display them immidiatly to the command line
errorHandler = logging.StreamHandler(sys.stdout)
errorHandler.setLevel(logging.ERROR)
errorHandler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(errorHandler)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# This command will create a party oject with the caller as the owner
@bot.command()
async def cParty(ctx, pSize:int ,*, name:str):
    # ctx.author passes a user object for private channels which has a different
    # name for the user's nickname.
    # Nonprivate passes a user

    authorNick = str(ctx.author.name)

    await ctx.send("Creating party of: size = " + str(pSize) +
    ",\n Name = " + name +
    ",\nOwner = " + authorNick)
    newRole = await ctx.guild.create_role(name = "party:"+name, color = discord.Colour.from_rgb(78, 255, 33))
    await ctx.message.author.add_roles(newRole)

    # try to add the party to the party list under the key of the guildID
    # If this fails then catch a Key error, this means the guild has not got
    # a key in the dict yet, so add one then add the party
    try:
        partyList[ctx.guild.id].append(Party(pSize, newRole, authorNick))
    except KeyError:
        partyList[ctx.guild.id] = []
        partyList[ctx.guild.id].append(Party(pSize, newRole, authorNick))

# this will loop through a guild and find the index of the party named "searchName"
# returns -1 if party not found
def findIndexOfParty(guildID, searchName):
    parties = partyList[guildID]
    for i in range(len(parties)):
        if ("party:" + searchName) == parties[i].role.name:
            return i


# This command lists the parties members of a given party if the author is part of the party
@bot.command()
async def listPartyMembers(ctx, *, searchName:str):
    # if the party exists in the guild they are searching in
    partyIndex = findIndexOfParty(ctx.guild.id, searchName)

    if partyIndex != -1:
        partyMembers = partyList[ctx.guild.id][partyIndex].role.members

        # Only show members if they are in this party
        if ctx.message.author in partyMembers:
            for i in range(len(partyMembers)):
                member = partyMembers[i]

                # Using ascii director line to show party members
                if i == len(partyMembers):
                    message += "    └──"
                elif i == 0:
                    message = searchName + "\n└──"
                else:
                    message +=  "   ├──"

                # Now add the member name, if they are the leader add a (L)
                if member.name == partyList[ctx.guild.id][partyIndex].owner:
                    message += member.name + " (L) \n"
                else:
                    message += member.name + " \n"

            await ctx.send(message)
        else:
            await ctx.send("You are NOT in this party")
    else:
        await ctx.send("I could not find this party. Possible reasons: Party name mis-spelt, Party disbanded or incorrect server")

# This will take a party (noted by it's guild and index) and check if it is empty
# if it is, delete it and return 1, else return 0
async def deleteIfEmpty(guildID, index):
    if len(partyList[guildID][index].role.members) <= 0:
        await partyList[guildID][index].role.delete()
        del partyList[guildID][index]
        return 1
    return 0

# This command allows a user to leave a party
@bot.command()
async def leaveParty(ctx,*, partyName:str):
    try:
        i = findIndexOfParty(ctx.guild.id, partyName)
        if i >= 0:
            # check if author is in the party
            if ctx.author in partyList[ctx.guild.id][i].role.members:
                role = partyList[ctx.guild.id][i].role
                await ctx.author.remove_roles(role)
                await ctx.send("I have succesfully removed you from the party")

                # If the person deleteing the guild is the owner, then check if it is
                # now empty, if not, tranfer to a new owner
                if partyList[ctx.guild.id][i].owner == ctx.author.name:
                    if not(await deleteIfEmpty(ctx.guild.id, i)):
                        partyList[ctx.guild.id][i].promoteOwner(partyList[ctx.guild.id][i].members[0])

            else:
                await ctx.send("Good news, you were not part of this party already!")
        else:
            await ctx.send("I was unable to find the party requested")
    except discord.errors.HTTPException:
        await ctx.send("Could not remove you from the party. possible reasons: Incorrect Name, this party has been disbanded")

# If you are the Leader, you will be able to delete the party
@bot.command()
async def disbandParty(ctx,*, partyName:str):
    try:
        i = findIndexOfParty(ctx.guild.id, partyName)
        if i >= 0:
            if partyList[ctx.guild.id][i].owner == ctx.author.name
                await partyList[ctx.guild.id][i].role.delete(reason = "Party disbanded")
                await ctx.send("Party Disbanded!")
            else:
                await ctx.send("Premission denied. You must be the leader in order to disband a party")
        else:
            await ctx.send("I could not find the party requested")

    except discord.errors.HTTPException:
        await ctx.send("Could not remove you from the party. possible reasons: Incorrect Name, this party has been disbanded")


bot.run(BOT_KEY)
