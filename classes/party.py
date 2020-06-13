# This class holds the info of a party for the discord bot, from here it can
# set a new leader

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

    def addInvited(self, members):
        self.invitedMembers.extend([mem.name for mem in members])
