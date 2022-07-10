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

# TODO: to be included in the documentation
# if you need a description of the quest that true over time this dictionary seemed to me the best way to do it
default quests_descriptions = {}

define quests = {
    "alice"     :   Quest(id = "alice", title = _("Help [a]"), bg="bg alice terrace talk", stages_id = ["talk alice1", "order products", "take products", "talk alice2"], description = _("To learn more about how the repo works, Talk to [a]. \nGoing when she is there will automatically start an \"Event\" (see routine*.rpy to learn more). \nAfter that an action (action*.rpy) will be added to open the pc, in MC room. \n\n(during the quest you can talk to [a] and you will see her talking during the quests of the same Quest)")),
    "ann"       :   Quest(id = "ann", title = _("Help [an]"), stages_id = ["talk al about ann", "take the key", "visit ann"], development = True),
}
define quest_stages = {
    # Quest "alice"
    "talk alice1"           :   Stage(idQuestOrTask = "alice", title = _("Talk [a]"), description = _("Talk [a] on the terrace."), label_start="stagestart_talkalice"),
    "order products"        :   Stage(idQuestOrTask = "alice", title = _("Order products"), description = _("Order the products with your PC.")),
    "take products"         :   Stage(idQuestOrTask = "alice", title = _("Take products"), description = _("Take products on the Terrace."), description_request = _("Wait for the products you ordered to arrive (2 day)"), days_late = 2, label_start="add_product"),
    "talk alice2"           :   Stage(idQuestOrTask = "alice", title = _("Talk [a]"), description = _("Talk [a].")),
    # Quest "ann"
    "talk al about ann"     :   Stage(idQuestOrTask = "ann", title = _("Talk [a]"), description = _("Talk [a]."), label_start="stagestart_talkalice_aboutann"),
    "take the key"          :   Stage(idQuestOrTask = "ann", title = _("take the key"), description = _("take the key.")),
    "visit ann"             :   Stage(idQuestOrTask = "ann", title = _("Visit [an]"), description = _("Go to the house of [an].")),
}

# Quest "alice"
label stagestart_talkalice:
    $ sp_routine["stagealice1"] = Commitment(chs={"alice" : TalkObject()}, tm_start=14, tm_stop=20, id_location="house", id_room="terrace", label_event="stage_talkalice")
    return

# Quest "ann"
label stagestart_talkalice_aboutann:
    $ addTalkChoice(id_choice = "alice", choice_text = _("About the Ann"), label_name = "stage_talkalice_aboutann", dict_choices = talkch_choices)
    return
