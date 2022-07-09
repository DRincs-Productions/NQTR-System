# Navigation Quest Time Routine System for Ren'py

![Last commit](https://img.shields.io/github/last-commit/DonRP/NQTR-toolkit)
![License](https://img.shields.io/github/license/DonRP/NQTR-toolkit)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>

This repo is a complete set of tools to create a game where you can explore and relate to characters.

In order to simplify the update work and avoid errors in saving I created functions that check the correct state of variables by inserting them in [after_load](game/tool/core.rpy#L1) (e.g. after a change to a quest that causes a stage to be blocked, the quest should restart) and an abundant use of define.

For the time being, a good part of the screens and images are not of my creation and terminology, and the comments need to be revised.

Feel free to contribute, fork this and send a pull request. 😄

## Instructions to insert Toolkit in your repo

I recommend the following ways to include it in your project:

- [**Pull branch**](https://github.com/DonRP/NQTR-toolkit#pull-branch) (to **insert** it into your game and **update** it easily)
- **Fork** (to improve the repo or create a Toolkit based on mine)

### Pull branch

To **insert** or **update** the Toolkit in your repo with Pull branch I recommend the following procedure:

(only if you want to insert the repo) Create a new empty branch, in the example I'll use **NQTR-toolkit**

```shell
git checkout -b NQTR-toolkit
git checkout NQTR-toolkit
git pull https://github.com/DonRP/NQTR-toolkit.git tool-only --allow-unrelated-histories
```

At the end make a merge inside the arm of the project.

## Documentation

[wiki](/wiki)

### Quest system

![alt text](/images/Quest.webp "Quest")

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
quests["alice"].start()
quests["ann"].start()
```

Move on to the next Stage, only if the Stage has been completed

```renpy
quests["alice"].next_stage()
```

To check which stage number a Quest has arrived at:

```renpy
if (quests_levels["alice"] == 2):
    # ...
```

###### Stage

The Stage() class is the necle of the Quest system. It is mandatory to define idQuestOrTask: it is the id of the quest it belongs to, or it is the id of the [Task](#Task) (explained later).
In addition as title, description, description_request and advice the other parameters:

bg: in the information you can see the image inserted in bg

goals = []: the [Goals](#Goal) to be passed (explained later)

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

###### Task

(in process)

###### Goal

(in process)

### Routine system

![alt text](/images/Routine.webp "Routine")

To skim the routines, simply compile df_routine and correctly add Commitment to sp_routine (the difference is explained later).
The Commitment() class has the following parameters:

tm_start & tm_stop (required): start time & end time

chs={"alice" : TalkObject(bg_before_after="bg alice roomsleep", label_talk="talk_sleep")

chs = {} (mandatory): list of characters (with whom you can [talk]()) participating in the routine,

id_location & id_room: Id della [Location](#Location) & [Room](#Room)

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

### Action

![alt text](/images/Action.webp "Action")

The Action() class is the fundamental element. It is mandatory to define name, icon and label, the unlima is the name of the label that will be called once the button is pressed.

Label example:

```renpy
label order_product:
    # Costume Code
    # Important: must always end with "call screen room_navigation"
    call screen room_navigation
```

Other parameters (not mandatory) are:

sp_room: it is used only in sp_actions (explained later), and is the place where the action will take place.
IMPORTANT: specify in sp_room the id of the room where the action will take place.

icon_selected: if it is not icon_selected=None then in the icon_selected will be used for selected_idle & selected_hover

tm_start & tm_stop: time when the event can be executed

day_start & day_deadline: day when the event will start. and the day when it will end, if it is in sp_actions it will be deleted

is_in_room & xpos & ypos: if is_in_room=True then the action will not be in the buttons at the side, but is an image with xalign yalign position.

Attention: for the icon you have to create the idle image with a name of your choice ("icon myroom"), and for selected_idle & selected_hover with the previous name + " a" ("icon myroom"). if you want to change this condition you have to change it in screens. I recommend the following way:

```renpy
image icon myroom = "location/myroom-icon.webp"

image icon myroom a = im.MatrixColor("location/myroom-icon.webp", im.matrix.brightness(-0.5))
```

Add an Action:

```renpy
sp_actions["order_product"] = Action(_("Order product"), "/interface/action-pc.webp", label = "order_product", sp_room='my_room')
```

Remove an Action:

```renpy
sp_actions.pop('take_product')
```

Remove an Action:

```renpy
label take_product:
    # Costume Code
    $ sp_actions.pop('take_product')
    call screen room_navigation
```

###### Habitual Action

```renpy
define df_actions = {
        "nap"       :   Action(_("Nap"), "/interface/action-sleep.webp", label = "nap", tm_start=5, tm_stop=23), 
        "sleep"     :   Action(_("Sleep"), "/interface/action-alarm.webp", label = "sleep", tm_start=23, tm_stop=5), 
    }
```

Habitual Actions are the actions that are usually performed. as explained before I used define for convenience. so they cannot be removed and added during the execution of the game, but only manually in the code.

###### Special Action

```renpy
default sp_actions = {}
```

The Special Actions are the actions that are not usual. I used default, so they can be removed and added during the execution of the game.
IMPORTANT: specify in sp_room the id of the room where the action will take place

### Talk system

The Talk system is related to routines. As explained in [Routine system](#Routine-system) the TalkObject() classes are inserted in the following ways:

```renpy
# This will start the default dialog
Commitment(chs={"alice" : None}, ...)
Commitment(chs={"alice" : TalkObject(bg_before_after="bg alice roomsleep"}, ...)
# Doing so will start label_talk of the TalkObject() class (explained later).
Commitment(chs={"alice" : TalkObject(bg_before_after="bg alice roomsleep", label_talk="talk_sleep")}, ...)
```

The TalkObject () class has no required parameters, and has the following parameters:

label_talk: is the label where the dialogue is located. IMPORTANT: If not specified it will start "label talk" (explained later).

ch_secondary: for group dialogs, you need to specify other chs besides the primary ch (in process).

bg_talk: is the image shown while speaking.

bg_before_after: by default when the dialogue is finished the image before the dialogue is shown. otherwise specify in the bg_before_after parameter the image you want to show after the dialog.

after_label_event: TODO:

###### Talk system default

As specified before if you don't specify label_talk in TalkObject() the default dialog will be started: first "label talk", after "label talk_menu".

```renpy
default talkch_choices = {}

label talk:
    if (talk_image != None):
        scene expression (talk_image) as bg

    if(talk_ch == None):
        call error_label
        call screen room_navigation

    # Costume Code
    if(talk_ch == "alice"):
        mc "Hi [a]"
        a "Hi, can you tell me something?"
    else:
        "Now is busy test later."

    call talk_menu
    jump talk_end
```

label talk: is a label used to give the possibility to customize the dialog even more.

label talk_menu: is a label that shows the choices contained in talkch_choices.

To add the choices in talkch_choices:

```renpy
addTalkChoice(ch = "alice", choice_text = _("About the Ann"), label = "stage_talkalice")
```

To remove the choices in talkch_choices:

```renpy
delTalkChoice(ch = "alice", choice_text = _("About the Ann"))
```

# Time

The class that handles Time is TimeHandler, and if you don't want defaust values you have to change "default tm = TimeHandler()" in [tool/time_handler.rpy](/game/tool/time_handler.rpy). Which has 4 non-obligatory parameters:

hour_new_day: This is the time that is set using the ".new_day ()" function. The ".new_day()" function in addition to passing the changeover to a new day, checks for morning events and checks for "expired" items.

hour & day: the hour and day set at the start of the game.

weekend_day: a value for the weekend day (in process)

has some very important functions, but I suggest managing everything (where possible) with [#Time-Label] (# Time-Label)

Some very intuitive functions:

```renpy
def get_day_number(self):
    #...
def get_weekday_number(self):
    #...
def get_weekday_name(self):
    #...
def new_hour(self, amt=event_duration):
    #...
def new_day(self):
    #...
```

get_hour_name (self): Returns the name of the current timeframe contained in "hour_names". e.g. morning, afternoon ...
To insert images that change over time:

```renpy
image bg annroom = "location/annroom-[tm.image_time].webp"
```

now_is_between (self, end, start = 0): check if the current time is between start and end.

I have set by default that when you wait you wait for 1 hour, if you want to change for example to manage morning, afternoon, evening and night just change wait_hour to [tool/time_label.rpy](/game/tool/time_label.rpy)

```renpy
define wait_hour = 1
```

I have also inserted a time block, which is unlocked by default: bl_values.get("block_spendtime") (guarda [bl_values]()). If it is active it displays the following text of the variable "block_spendtime_dialogue" which is in [tool/time_label.rpy](/game/tool/time_label.rpy)

```renpy
define block_spendtime_dialogue = _("You can't do that now")
```

###### Time Label

To manage time I recommend using the label in [tool/time_label.rpy](/game/tool/time_label.rpy), or the Shares you find in [tool/action_label.rpy](/game/tool/action_label.rpy)

```renpy
label new_day:
    #...

label wait:
    #...

label after_wait:
    # Used after an event or a wait, it updates valid values and makes various checks to know if there are any events in the current time
```

The following advice to customize to your liking:

```renpy
label wait_onehour:
    #...

label nap:
    #...

label sleep:
    #...
```
