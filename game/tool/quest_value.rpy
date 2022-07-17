# the number of stages completed in a quest
default number_stages_completed_in_quest = {}
default current_quest_stages = {}
default current_task_stages = {}

# if you need a description of the quest that true over time this dictionary seemed to me the best way to do it
default quests_descriptions = {}

define quests = {
    "alice"  : Quest(id = "alice", title = _("Help [a]"), bg = "bg alice terrace talk",
        stages_id = ["talk alice1", "order products", "take products", "talk alice2"], 
        description = _("To learn more about how the repo works, Talk to [a]. \nGoing when she is there will automatically start an \"Event\" (see routine*.rpy to learn more). \nAfter that an action (action*.rpy) will be added to open the pc, in MC room. \n\n(during the quest you can talk to [a] and you will see her talking during the quests of the same Quest)"),
        development = False,
    ),
    "ann"  : Quest(id = "ann", title = _("Help [an]"), bg = None,
        stages_id = ["talk al about ann", "take the key", "visit ann"], 
        description = _("Long Description"),
        development = True,
    ),
}
define quest_stages = {
    # Quest "alice"
    "talk alice1"           :   Stage(quest_id = "alice", title = _("Talk [a]"), description = _("Talk [a] on the terrace."), start_label_name="stagestart_talkalice"),
    "order products"        :   Stage(quest_id = "alice", title = _("Order products"), description = _("Order the products with your PC.")),
    "take products"         :   Stage(quest_id = "alice", title = _("Take products"), description = _("Take products on the Terrace."), request_description = _("Wait for the products you ordered to arrive (2 day)"), days_required_to_start = 2, start_label_name="add_product"),
    "talk alice2"           :   Stage(quest_id = "alice", title = _("Talk [a]"), description = _("Talk [a].")),
    # Quest "ann"
    "talk al about ann"     :   Stage(quest_id = "ann", title = _("Talk [a]"), description = _("Talk [a]."), start_label_name="stagestart_talkalice_aboutann"),
    "take the key"          :   Stage(quest_id = "ann", title = _("take the key"), description = _("take the key.")),
    "visit ann"  :  Stage(quest_id = "ann", title = _("Visit [an]"), days_required_to_start = 0,
        number_stages_completed_in_quest_requests = {
        }
    ),
}

# Quest "alice"
label stagestart_talkalice:
    $ routine["stagealice1"] = Commitment(ch_talkobj_dict={"alice" : TalkObject()}, tm_start=14, tm_stop=20, location_id="house", room_id="terrace", event_label_name="stage_talkalice")
    return

# Quest "ann"
label stagestart_talkalice_aboutann:
    $ addTalkChoice(choice_id = "alice", choice_text = _("About the Ann"), label_name = "stage_talkalice_aboutann", dict_choices = talkch_choices)
    return
