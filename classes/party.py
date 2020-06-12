# This class holds the info of a party for the discord bot, from here it can
# addMembers,   removeMember,   set a new leader
class Party:
    def __init__(self,pSize:int, name,owner:str):
        self.pSize = pSize
        self.name = name
        self.owner = owner
        self.members = [owner]

    def addMembers(self, memberToAdd):
        if self.isFull():
            return 0
        else:
            self.members.append(memberToAdd)
            return 1

    def removeMember(self,memberToRm):
        try:
            self.members.remove(memberToRm)
            if memberToRm == self.owner:
                self.owner = self.members[0]
            return 1
        except ValueError:
            return 0


    def promoteOwner(self, newLeader):
        if newLeader in self.members:
            self.owner = newLeader
            return 1
        else:
            return 0

    def isFull(self):
        if len(self.members) == self.pSize:
            return 0
        else:
            return 1
