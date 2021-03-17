# Stage

# quest_stages: is the list of all existing Stage tasks.
# it is used to keep all information about all Stages

# current_quest_stages: are the Stage currently active,
# contains only the data strictly necessary for proper operation
# after their completion they are replaced with the next one

# Task
# current_task_stages is identical to this_current, 
# except that after completion they are not replaced by the next one, but eliminated. 
# The idea is that the Tasks are not within the "Stage" and therefore have no subsequent internships.

# Quest
# the Quest is a list of Stages that follow each other according to their order
# quests and quests_levels are synchronized, meaning they will always have the same elements

# quests_levels: must not have elements at the beginning. what is it for? to know which number of this has arrived at an internship
# quest_stages is similar to quest_stages and contains information about internships

default quests_levels = {}
default current_quest_stages = {}
default current_task_stages = {}

define quests = {
    "alice"     :   Quest(id = "alice", title = _("Help [a]"), bg="bg alice terrace talk", stages_id = ["talk alice1", "order products", "take products", "talk alice2"], description = _("To learn more about how the repo works, Talk to [a]. \nGoing when she is there will automatically start an \"Event\" (see routine*.rpy to learn more). \nAfter that an action (action*.rpy) will be added to open the pc, in MC room. \n\n(during the quest you can talk to [a] and you will see her talking during the quests of the same Quest)")),
    "ann"       :   Quest(id = "ann", title = _("Help [an]"), stages_id = ["talk al about ann"], development = True),
}
define quest_stages = {
    # Quest "alice"
    "talk alice1"           :   Stage(idQuestOrTask = "alice", title = _("Talk [a]"), description = _("Talk [a] on the terrace."), label_start="stagestart_talkalice"),
    "order products"        :   Stage(idQuestOrTask = "alice", title = _("Order products"), description = _("Order the products with your PC.")),
    "take products"         :   Stage(idQuestOrTask = "alice", title = _("Take products"), description = _("Take products on the Terrace."), description_request = _("Wait for the products you ordered to arrive (2 day)"), days_late = 2, label_start="add_product"),
    "talk alice2"           :   Stage(idQuestOrTask = "alice", title = _("Talk [a]"), description = _("Talk [a].")),
    # Quest "ann"
    "talk al about ann"     :   Stage(idQuestOrTask = "ann", title = _("Talk [a]"), description = _("Talk [a].")),
    "visit ann"             :   Stage(idQuestOrTask = "ann", title = _("Visit [an]"), description = _("Go to the house of [an].")),
}

# Quest "alice"
label stagestart_talkalice:
    $ sp_routine["stagealice1"] = Commitment(chs={"alice" : TalkObject()}, tm_start=14, tm_stop=20, id_location="house", id_room="terrace", label_event="stage_talkalice")
    return

label stage_talkalice:
    if (quests_levels["alice"] == 0):
        show bg alice terrace talk
        a "Hi can you order me a new book from pc?"
        mc "Ok"
        a "Thanks"

        if ("alice" in talkch_choices.keys()): 
            $ talk_choices = talkch_choices["alice"]
        else:
            $ talk_choices = []
        $ talk_choices.append((_("About the book"), "stage_talkalice"))
        $ talkch_choices["alice"] = talk_choices
        $ del talk_choices

        $ sp_actions["order_product"] = Action(_("Order product"), "/interface/action-pc.webp", label = "order_product", sp_room='my_room')

        $ quests["alice"].next_stage()
    elif (quests_levels["alice"] == 1):
        mc "What book do you want me to order?"
        a "For me it is the same."
        jump talk_menu
    elif (quests_levels["alice"] == 2):
        mc "I ordered the Book, hope you enjoy it."
        a "Great, when it arrives remember to bring it to me."
        jump talk_menu
    elif (quests_levels["alice"] == 3):
        mc "Here's your book."
        a "Thank you, I can finally read something new."
        $ quests["alice"].next_stage()
        $ talkch_choices["alice"].pop()
    return
