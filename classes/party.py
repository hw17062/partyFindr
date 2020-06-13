# This class holds the info of a party for the discord bot, from here it can
# addMembers,   removeMember,   set a new leader

import discord  # Import the relevent discord Framework

class Party():
    def __init__(self,pSize:int, role,owner:str):
        self.pSize = pSize
        self.role = role
        self.owner = owner

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
