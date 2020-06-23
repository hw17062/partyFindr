# Read Me

Hello, The aim of this project is to be able to provide useful sub-groups (Dubbed: parties) with-in a discord server.


## To-Do List

- [x] ~~Party Class~~
- [x] ~~Store Parties in mem~~
- [x] ~~Create a party~~
- [x] ~~List Party members~~
- [x] ~~Leave Party~~
- [x] ~~Disband Party~~
- [x] ~~create Embeded party invite~~
- [x] ~~Invite people to party~~
- [x] ~~Join party invited to~~
- [x] ~~Update Party Ad on joining/leaving~~
- [ ] Store Parties on Disk
- [ ] Party Role Feature
- [ ] Create Text Chat
- [ ] Create Voice Channel

## Bot.Commands
Here I will describe the comands for the Bot. The Defult command_Prefix is '?'. This is currently uneditable.

### ?cParty <a name = "cParty"></a>
*Command*</t> '?cParty {partySize} "{partyName}" "{Description}" *{mentions}'*

cParty will create the party, setting the athor as the owner. It will create a new role on the server named "Party:{partyName}" , add this role on the author. Then, it will create an 'Ad' for the party with an Embed message. If someone invited :Thumbs Up: reaction the ad, they will join the party.<br>
This ad will be updated upon members joining and leaving, and will be removed when the party is full.

#### Example
```
?cParty 5 "WoW Dungeon Run" "Group of only the best dungeoneers!" @HealerInNeed @iNeedHealing @Palawin
```

### ?listPartyMembers
*Command* '?listPartyMembers "{partyName}" '

This command will list all members in a party with the name "partyName". This will only display the members if you are part of the party.
#### Example
```
?listPartyMembers "WoW Dungeon Run"
```

### ?leaveParty
*Command* '?leaveParty "{partyName}" '

This command will remove you from the party with the given name, should you be in this party.
If the leader leaves, a new leader is assigned. If a party becomes empty, it will automatically be disbanded.

#### Example
```
?leaveParty "WoW Dungeon Run"
```

### ?disbandParty
*Command* '?disbandParty "{partyName}"

If you are the leader of a party, this command will delete the party from the role list.

#### Example
```
?disbandParty "WoW Dungeon Run"
```

### ?invite
*Command* '?invite "{partyName}" *{mentions}* '

If you are the leader, this command will update the party Ad Message allowing the members you mention to join the party should they wish.

#### Example
```
?invite "WoW Dungeon Run" @betterHealer
```

### ?postAd
*command* '?postAd "{partyName}" *{mentions}*'

This will generate a new Ad and post it to the channel the command was made. Optional mentions for updating invite for the new Ad.

#### Example
```
?postAd "WoW Dungeon Run" @newChannelMembers
```

## bot.event
This lists the functions class on events.

### on_reaction_add
*event* on_reaction_add(reaction, user)

#### Thumbs Up reaction
This reaction will add a user to the party if reacted on an Ad.

On a thumbs up, the bot will check if the reacted message is from the list of parties' Ads. If so, check if the user is eligible to join, if so, they are added to the party.

#### Thumbs Down reaction
This reaction will remove the user from the list of invited members in a party Ad.

# Man Pages

## <a name="Class_Party"></a> Party
*class* Party(partySize ,role , owner)  <br>
Represents a party. Init on ['?cParty'](#cParty)

### Attributes

####   description
**Type**  String  <br>
The description set at the creation of the party, used when creating or updating the party Ad.

#### name
**Type** String

The Name of the party, used when creating or updating the party Ad.
####   partySize
**Type**  int

This shows the party's Max size.  Set on Init
### role
 **Type** [Discord.Role](https://discordpy.readthedocs.io/en/latest/api.html?highlight=role#discord.Role)

 This holds the role created in the guild for this party.  Set on Init

### Owner
**Type** str

Holds the Name of the current leader of the party.  Set on Init
### invitedMembers
**Type** [str]

Holds a list of all members that have been invited to the party to act as a white list.
### advertMessage
**Type** List[[Discord.Message](https://discordpy.readthedocs.io/en/latest/api.html?highlight=message#message)]

Holds the Message objects creating with '?postAd' and '?cParty', add to with 'linkAd()'
### openParty
**Type** Bool

Holds wether the party is open to everyone in it's channel's origins or is invite only. Decided by invites, if @Everyone is used, this will be set to True.

### Methods

#### promoteOwner
*party.promoteOwner(self, newLeader)*

**newLeader** - Str, name of user being promoted
This will see if the new user is in the party, if they are, they are set as [Party.owner](#Owner)

**returns** bool ? was transfer successful

#### isFull
*party.promoteOwner(self)*

**returns** bool ? is party full

#### addInvited
*party.addInvited(self, members)*

**members** = list[Discord.Member]
loops through members, adding them to Party.Role.members

#### makeOpen
*party.makeOpen (self)*
Sets openParty to True

#### makeClose
*party.makeOpen (self)*
Sets openParty to False

#### async makeAd
*party.makeAd (self)*
This will create and return a Discord.Embed object representing a new Ad for the party with the latest info.

#### linkAd
*party.linkAd (self, message)*
**message** = Discord.message
This will add the passes message object to the list of advertMessage, allowing the object to track where each copy of it's advert is for updating.

#### async updateAd
*party.updateAd (self)*
This method will create an new version of the Embed Ad and edit all linked copies.

#### deleteAds
*party.deleteAds (self)*
This method will go through and delete all linked Ad messages.
