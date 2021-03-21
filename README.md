# Navigation Quest Time Routine System for Ren'py

![Last commit](https://img.shields.io/github/last-commit/DonRP/NQTR-toolkit)
![License](https://img.shields.io/github/license/DonRP/NQTR-toolkit)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>

This repo is a complete set of tools to create a game where you can explore and relate to characters. 

In order to simplify the update work and avoid errors in saving I created functions that check the correct state of variables by inserting them in after_load 
(e.g. after a change to a quest that causes a stage to be blocked, the quest should restart) and an abundant use of define.

For the time being, a good part of the screens and images are not of my creation and terminology, and the comments need to be revised.

## Documentation

### Navigation and Map

To create the navigation you only need to fill in the following variables correctly.

###### Room

In the Room() class you must define id & id_location (location of the room).

id_actions is a list of id's of df_actions that are located in that room.

```renpy
define rooms = [
        Room(id="my_room", id_location="house", name=_("MC room"), icon="icon myroom", bg="bg myroom", id_actions = ["sleep","nap",]), 
        Room(id="bathroom", id_location="house", name=_("Bathroom"), icon="icon bathroom", bg="bg bathroom"), 
        Room(id="lounge", id_location="house", name=_("Lounge"), icon="icon lounge", bg="bg lounge"), 
        Room(id="terrace", id_location="house", name=_("Terrace"), icon="icon terrace", bg="bg terrace"), 
    ]
```

To select the room the player will be in at the beginning:
```renpy
label start:
    $ cur_room = rooms[0]
    $ cur_location = locations[cur_room.id_location]
```

###### Location

In the Location() class it is mandatory to define id , key_map & id_externalroom (id of the room which will be opened when moving from one location to another across the map).

xalign yalign is for defining the position of the icon on the map.
```renpy
define locations = {
        "house"     :   Location(id = "house", key_map="map", id_externalroom="terrace", name=_("MC house"), icon="icon map home", xalign=0.3, yalign=0.2), 
    }
```

###### Map

I preferred not to create a map class. the reason why I preferred to create a list of maps is to give the possibility to create more maps to travel in.
```renpy
define map_images = {
        "map"       :   "bg map",
    }
```

Please note that to check whether the map can be used I used check_goout in open_map:
```renpy
define block_goout_dialogue = _("Now is not the time to go outside")
label check_goout:
    if(bl_values.get("goout") == False):
        "[block_goout_dialogue]"
        call screen room_navigation
    return
```

### Quest system
The system of quests is a bit more complicated, it consists of Quests containing one or more Stages which in turn may contain one or more Goals. The stage can belong to the Quest or Stage dictionary.
To create Quests you just have to enter the right values in Quests and Quest_stages.

##### Quest
The Quest() class is a set of stages, which follow each other in an orderly fashion. It is mandatory to define id and title.
as well as description and stages_id the other parameters:

bg: in the information you see the image inserted in bg

development = True: when the quest is completed a text will be displayed explaining that this is the temporary end of the quest.

icon & category: have not been implemented yet.

```renpy
define quests = {
    "alice"     :   Quest(id = "alice", title = _("Help [a]"), bg="bg alice terrace talk", 
    stages_id = ["talk alice1", "order products", "take products", "talk alice2"], 
    description = _("To learn more about how the repo works, Talk to [a]. \nGoing when she is there will automatically start an \"Event\" (see routine*.rpy to learn more). \nAfter that an action (action*.rpy) will be added to open the pc, in MC room. \n\n(during the quest you can talk to [a] and you will see her talking during the quests of the same Quest)")),

    "ann"       :   Quest(id = "ann", title = _("Help [an]"), stages_id = ["talk al about ann"], development = True),
}
```

To start a Quest:
```renpy
$ quests["alice"].start()
$ quests["ann"].start()
```
Move on to the next Stage, only if the Stage has been completed
```renpy
$ quests["alice"].next_stage()
```
To check which stage number a Quest has arrived at:
```renpy
if (quests_levels["alice"] == 2):
    # ...
```
