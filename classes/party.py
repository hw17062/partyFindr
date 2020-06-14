# This class holds the info of a party for the discord bot, from here it can
# set a new leader

import datetime

class Party():
    def __init__(self,pSize:int, role,owner:str):
        self.partySize = pSize
        self.role = role
        self.owner = owner
        self.invitedMembers = []
        self.inviteMessage =''  # Will be of type discord.message
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
    async def addInvited(self, members):
        # extend the invitedMembers var
        self.invitedMembers.extend([mem.name for mem in members])
        embed = discord.Embed()

    def makeOpen():
        self.openParty = True

    def makeClose():
        self.openParty = False

    # This function will return a Discord.Embed object for the Ad of the Party
    async def makeAd():
        membersAsString = ""
        mentionsAsString = ""
        if self.openParty:
            mentionsAsString = "Open Party"
        else:
            mentionsAsString = ", ".join(self.invitedMembers)

        membersAsString = ", ".join([mem.name for mem in self.role.members])
        partySizeString = "{0} / {1}".format(len(self.role.members), self.partySize)
        # create embed object
        eInvMes = discord.Embed(title=partyName,
                                timestamp= datetime.datetime.utcnow(),
                                color=discord.Colour.from_rgb(78, 255, 33),
                                description= description)

        eInvMes.add_field(name="Owner", value=self.owner, inline=False)
        eInvMes.add_field(name="members", value=membersAsString, inline=True)
        eInvMes.add_field(name="Invited", value=mentionsAsString, inline=True)
        eInvMes.add_field(name="party size", value=partySizeString , inline=True)
        eInvMes.add_field(name="How to Join", value=" react with a 👍 to join the party!" , inline=False)

        return eInvMes

    def linkAd(self, message):
        self.inviteMessage = message
