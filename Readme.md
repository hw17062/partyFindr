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
*class* Party(partySize ,role , owner)
Represents a party. Init on '?cParty' 

### partySize
**Type**  int
This shows the party's Max size.  Set on Init
### role
 **Type** Discord.Role
 This holds the role created in the guild for this party.  Set on Init
 ### Owner
 **Type** str
 Holds the Name of the current leader of the party.  Set on Init
 ### invitedMembers
 **Type** [str]
 Holds a list of all members that have been invited to the party to act as a white list.
