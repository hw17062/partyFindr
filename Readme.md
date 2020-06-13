# Read Me

Hello, The aim of this project is to be able to provide useful sub-groups (Dubbed: parties) with-in a discord server. 


## To-Do List

- [x] ~~Party Class~~
-  [x] ~~Store Parties in mem~~
-  [x] ~~Create a party~~
-  [x] ~~List Party members~~
-  [x] ~~Leave Party~~
-  [x] ~~Disband Party~~
-  [x] ~~create Embeded party invite~~
-  [x] ~~Invite people to party~~
- [ ] Join party invited to
- [ ] Update Party Ad on joining/leaving
- [ ] Store Parties on Disk
- [ ] Party Role Feature
- [ ] Create Text Chat
- [ ] Create Voice Channel

# Man Pages

## <a name="Class_Party"></a> Party
*class* Party(partySize ,role , owner)  <br>
Represents a party. Init on ['?cParty'](#cParty)

### partySize
**Type**  int  <br>
This shows the party's Max size.  Set on Init
### role
 **Type** [Discord.Role](https://discordpy.readthedocs.io/en/latest/api.html?highlight=role#discord.Role) <br>
 This holds the role created in the guild for this party.  Set on Init
 ### Owner
 **Type** str <br>
 Holds the Name of the current leader of the party.  Set on Init
 ### invitedMembers
 **Type** [str] <br>
 Holds a list of all members that have been invited to the party to act as a white list.
### inviteMessage
**Type** [Discord.Message](https://discordpy.readthedocs.io/en/latest/api.html?highlight=message#message)
Holds the Message object created by the Embed Ad on ['?cParty'](#cParty). Made automatically on Creation with ['?cParty'](#cParty).

### openParty
**Type** Bool
Holds wether the party is open to everyone in it's channel's origins or is invite only. Decided by invites, if @Everyone is used, this will be set to True

## Bot.Commands
Here I will describe the comands for the Bot. The Defult command_Prefix is '?'. This is currently uneditable.

### ?cParty <a name = "cParty"></a>
*Command* '?cParty {partySize} "{partyName}" "{Description}" *{Invites}'
cParty will create the party, setting the athor as the owner. It will create a new role on the server named "Party:{partyName}" , add this role on the author. Then, it will create an 'Ad' for the party
