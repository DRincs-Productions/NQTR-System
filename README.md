# Navigation Quest Time Routine System for Ren'py

![Last commit](https://img.shields.io/github/last-commit/DonRP/NQTR-toolkit)
![License](https://img.shields.io/github/license/DonRP/NQTR-toolkit)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>
<span class="badge-buymeacoffee">
<a href="https://www.buymeacoffee.com/p/506924" title="Donate to this project using Buy Me A Coffee"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg" alt="Buy Me A Coffee donate button" /></a>
</span>

This repo is a complete set of tools to create a game where you can explore and relate to characters. 

In order to simplify the update work and avoid errors in saving I created functions that check the correct state of variables by inserting them in after_load 
(e.g. after a change to a quest that causes a stage to be blocked, the quest should restart) and an abundant use of define.

For the time being, a good part of the screens and images are not of my creation and terminology, and the comments need to be revised.

## Instructions to insert Toolkit in your repo 
I recommend the following ways to include it in your project:
- [**Pull branch**](https://github.com/DonRP/NQTR-toolkit#pull-branch) (to **insert** it into your game and **update** it easily)
- **Fork** (to improve the repo or create a Toolkit based on mine)

### Pull branch
To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **NQTR-toolkit**

`git checkout NQTR-toolkit`

`git pull https://github.com/DonRP/NQTR-toolkit.git tool-only --allow-unrelated-histories`

At the end make a merge inside the arm of the project.

## Documentation

### Navigation and Map
![alt text](https://github.com/DonRP/NQTR-toolkit/blob/master/images/Navigation.webp "Navigation")

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

###### Closed Room
It is possible to make a room closed: ... is a dictionary of closed rooms (id=room_id : Commitment()), it is used in change_room and in after_wait closed rooms are deleted (every hour). the expiration time is .tm_stop, if you don't want a deadline: .tm_stop = None.
The room will remain closed from tm_start to tm_stop, only if at least one NPC is present in it, if you want the room always closed: .chs = None.

Examples of how to add them:
```renpy
$ closed_rooms[cur_room.id] = df_routine["alice_sleep"]
jump after_wait
```
```renpy
$ closed_rooms[cur_room.id] = df_routine["alice_sleep"]
# does not expire
$ closed_rooms[cur_room.id].tm_stop = None
# will remain closed even if there are no NPCs inside.
$ closed_rooms[cur_room.id].chs = None
jump after_wait
```
```renpy
$ closed_rooms[cur_room.id] = Commitment(chs={"alice" : None}, tm_start=14, tm_stop=20)
jump after_wait
```

Where to change the image of the closed door or customise the event? in closed_room_event.

###### Location

In the Location() class it is mandatory to define id , key_map & id_externalroom (id of the room which will be opened when moving from one location to another across the map).

xalign yalign is for defining the position of the icon on the map.
```renpy
define locations = {
        "house"     :   Location(id = "house", key_map="map", id_externalroom="terrace", name=_("MC house"), icon="icon map home", xalign=0.3, yalign=0.2), 
    }
```

###### Map
![alt text](https://github.com/DonRP/NQTR-toolkit/blob/master/images/Map.webp "Map")

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
![alt text](https://github.com/DonRP/NQTR-toolkit/blob/master/images/Quest.webp "Quest")

The system of quests is a bit more complicated, it consists of Quests containing one or more Stages which in turn may contain one or more Goals. The stage can belong to the Quest or Stage dictionary.
To create Quests you just have to enter the right values in Quests and Quest_stages.

###### Quest
The Quest() class is a set of stages, which follow each other in an orderly fashion. It is mandatory to define id and title.
In addition as description and stages_id the other parameters:

bg: in the information you can see the image inserted in bg, in case it is not defined in Stage

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

###### Stage
The Stage() class is the necle of the Quest system. It is mandatory to define idQuestOrTask: it is the id of the quest it belongs to, or it is the id of the [Task]() (explained later).
In addition as title, description, description_request and advice the other parameters:

bg: in the information you can see the image inserted in bg

goals = []: the [Goals]() to be passed (explained later)

days_late: days_late must pass since we "reached" the stage to start it

bl_requests = []: the [bl_values]() (explained later) must be set to True to start the quest

```renpy
quests_levels_requests = {
    "quest id"  :   level,
}
```
quests_levels_requests: to start the stage: quests_levels[quest] < level

label_start: label which will be started at the beginning of the quest

label_end: label which will be started at the end of the stage

label_check: (has not been implemented yet)

```renpy
define quest_stages = {
    # Quest "alice"
    "talk alice1"           :   Stage(idQuestOrTask = "alice", title = _("Talk [a]"), 
    description = _("Talk [a] on the terrace."), label_start="stagestart_talkalice"),
    "order products"        :   Stage(idQuestOrTask = "alice", title = _("Order products"), 
    description = _("Order the products with your PC.")),
    "take products"         :   Stage(idQuestOrTask = "alice", title = _("Take products"), 
    description = _("Take products on the Terrace."), 
    description_request = _("Wait for the products you ordered to arrive (2 day)"), 
    days_late = 2, label_start="add_product"),
    "talk alice2"           :   Stage(idQuestOrTask = "alice", title = _("Talk [a]"), description = _("Talk [a].")),
    # Quest "ann"
    "talk al about ann"     :   Stage(idQuestOrTask = "ann", title = _("Talk [a]"), description = _("Talk [a].")),
    "visit ann"             :   Stage(idQuestOrTask = "ann", title = _("Visit [an]"), 
    description = _("Go to the house of [an].")),
}
```

###### Task (in process)

###### Goal (in process)

### Routine system
![alt text](https://github.com/DonRP/NQTR-toolkit/blob/master/images/Routine.webp "Routine")

To skim the routines, simply compile df_routine and correctly add Commitment to sp_routine (the difference is explained later).
The Commitment() class has the following parameters:

tm_start (required): start time

tm_stop (required): end time

chs={"alice" : TalkObject(bg_before_after="bg alice roomsleep", label_talk="talk_sleep")

chs = {} (mandatory): list of characters (with whom you can [talk]()) participating in the routine, 

[id_location & id_room]()

day_deadline: day on which it is deleted (only for sp_routine)

label_event: a scene that starts as soon as the MC is in that room at that time (only for sp_routine)

name & type: have not been implemented

For character icons you have to compile [ch_icons]().

###### Default routine
```renpy
define df_routine = {
        "alice_sleep"       :   Commitment(chs={"alice" : TalkObject(bg_before_after="bg alice roomsleep", label_talk="talk_sleep")}, tm_start=20, tm_stop=10, id_location="house", id_room="alice_room"),
        "alice_lounge"      :   Commitment(chs={"alice" : TalkObject(bg_before_after=None, bg_talk=None)}, tm_start=10, tm_stop=14, id_location="house", id_room="lounge"),
        "alice_go_school"   :   Commitment(chs={"alice" : TalkObject(bg_before_after=None, bg_talk=None)}, tm_start=10, tm_stop=14, name="school", type="no_week"),
        "alice_read"        :   Commitment(chs={"alice" : TalkObject(bg_before_after="bg alice terrace", bg_talk="bg alice terrace talk")}, tm_start=14, tm_stop=20, id_location="house", id_room="terrace"),
    }
```
These are the fixed routines in case there are no sp_routines for NCP at the current time, then the NCP will have to perform df_routines.
Do not have a deadline.

ATTENTION cannot be an event (a scene that starts as soon as the MC is in that room at that time), only sp_routines can be events.

###### Special routine
```renpy
default sp_routine = {}
```
Initially it will be voting and during the game routines will be added to change the position of the characters.

They are added after completing missions or for some other reason.

If there is another commitment in the default routine at the same time, it will be "overwritten"

