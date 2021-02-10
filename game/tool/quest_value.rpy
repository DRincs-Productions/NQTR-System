# Quest

# quest_memory: is the list of all existing quest tasks.
# it is used to keep all information about all quests

# quest_current: are the quest currently active,
# contains only the data strictly necessary for proper operation
# after their completion they are replaced with the next one

# Task
# task_current is identical to this_current, 
# except that after completion they are not replaced by the next one, but eliminated. 
# The idea is that the Tasks are not within the "Stage" and therefore have no subsequent internships.

# Stage
# the Stage is a list of quests that follow each other according to their order
# stage_memory and stage_level are synchronized, meaning they will always have the same elements

# stage_level: must not have elements at the beginning. what is it for? to know which number of this has arrived at an internship
# quest_memory is similar to quest_memory and contains information about internships

default stage_level = {}
default quest_current = {}
default task_current = {}

define stage_memory = {
    "alice"     :   Stage(id = "alice", title = _("Help [a]"), bg="bg alice terrace talk", quest_list = ["talk alice1", "order products", "take products", "talk alice2"], description = _("To learn more about how the repo works, Talk to [a]. \nGoing when she is there will automatically start an \"Event\" (see routine*.rpy to learn more). \nAfter that an action (action*.rpy) will be added to open the pc, in MC room. \n\n(during the quest you can talk to [a] and you will see her talking during the quests of the same stage)")),
    "ann"       :   Stage(id = "ann", title = _("Help [an]"), quest_list = ["talk al about ann"], development = True),
}
define quest_memory = {
    # stage "alice"
    "talk alice1"           :   Quest(id_stageOrTask = "alice", title = _("Talk [a]"), description = _("Talk [a] on the terrace."), label_start="queststart_talkalice"),
    "order products"        :   Quest(id_stageOrTask = "alice", title = _("Order products"), description = _("Order the products with your PC.")),
    "take products"         :   Quest(id_stageOrTask = "alice", title = _("Take products"), description = _("Take products on the Terrace."), description_request = _("Wait for the products you ordered to arrive (2 day)"), days_late = 2, label_start="add_product"),
    "talk alice2"           :   Quest(id_stageOrTask = "alice", title = _("Talk [a]"), description = _("Talk [a].")),
    # stage "ann"
    "talk al about ann"     :   Quest(id_stageOrTask = "ann", title = _("Talk [a]"), description = _("Talk [a].")),
    "visit ann"             :   Quest(id_stageOrTask = "ann", title = _("Visit [an]"), description = _("Go to the house of [an].")),
}

# stage "alice"
label queststart_talkalice:
    $ sp_routine["stagealice1"] = Commitment(chs={"alice" : TalkObject()}, tm_start=14, tm_stop=20, id_location="house", id_room="terrace", label_event="quest_talkalice")
    return

label quest_talkalice:
    if (stage_level["alice"] == 0):
        show bg alice terrace talk
        a "Hi can you order me a new book from pc?"
        mc "Ok"
        a "Thanks"

        if ("alice" in talkch_choices.keys()): 
            $ talk_choices = talkch_choices["alice"]
        else:
            $ talk_choices = []
        $ talk_choices.append((_("About the book"), "quest_talkalice"))
        $ talkch_choices["alice"] = talk_choices
        $ del talk_choices

        $ sp_actions["order_product"] = Action(_("Order product"), "/interface/action-pc.webp", label = "order_product", sp_room='my_room')

        $ stage_memory["alice"].next_quest()
    elif (stage_level["alice"] == 1):
        mc "What book do you want me to order?"
        a "For me it is the same."
        jump talk_menu
    elif (stage_level["alice"] == 2):
        mc "I ordered the Book, hope you enjoy it."
        a "Great, when it arrives remember to bring it to me."
        jump talk_menu
    elif (stage_level["alice"] == 3):
        mc "Here's your book."
        a "Thank you, I can finally read something new."
        $ stage_memory["alice"].next_quest()
        $ talkch_choices["alice"].pop()
    return
