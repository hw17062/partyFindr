# This class holds the info of a party for the discord bot, from here it can
# set a new leader

import discord  # Import the relevent discord Framework
import datetime

class Party():
    def __init__(self,pSize:int, role,owner:str, name:str, desc:str):
        self.description = desc
        self.name = name
        self.partySize = pSize
        self.role = role
        self.owner = owner
        self.invitedMembers = []    # list of discord.member
        self.advertMessage =[]  # Will be of type discord.message, list of all locations of the Ad
        self.openParty = False

    def promoteOwner(self, newLeader):
        if newLeader in [mem.name for mem in self.role.members] :
            self.owner = newLeader.name
            return 1
        else:
            return 0

    def isFull(self):
        if len(self.role.members) == self.pSize:
            return 0
        else:
            return 1

    # get a list of Discord.Member ojbects to add to the invite lists
    # then update the Party Ad
    def addInvited(self, members):
        # extend the invitedMembers var
        self.invitedMembers.extend(members)
        self.makeClose()

    def makeOpen(self):
        self.openParty = True

    def makeClose(self):
        self.openParty = False


    async def updateAd(self):
        ad = await self.makeAd()

        for msg in self.advertMessage:
            await msg.edit(embed = ad)

    def linkAd(self, message):
        self.advertMessage.append(message)

    def deleteAds(self):
        for msg in self.advertMessage:
            msg.delete()

    # This function will return a Discord.Embed object for the Ad of the Party
    async def makeAd(self):
        mentionsAsString = ""
        if self.openParty:
            mentionsAsString = "Open Party"
        else:
            mentionsAsString = ", ".join([mem.mention for mem in self.invitedMembers])

        membersAsString = ", ".join([mem.name for mem in self.role.members])

        partySizeString = "{0} / {1}".format(len(self.role.members), self.partySize)
        # create embed object
        eInvMes = discord.Embed(title=self.name,
                                timestamp= datetime.datetime.utcnow(),
                                color=discord.Colour.from_rgb(78, 255, 33),
                                description= self.description)

        eInvMes.add_field(name="Owner", value=self.owner, inline=False)
        eInvMes.add_field(name="members", value=membersAsString, inline=True)
        eInvMes.add_field(name="Invited", value=mentionsAsString, inline=True)
        eInvMes.add_field(name="party size", value=partySizeString , inline=True)
        eInvMes.add_field(name="How to Join", value="react with a 👍 to join the party!" , inline=False)

        return eInvMes
