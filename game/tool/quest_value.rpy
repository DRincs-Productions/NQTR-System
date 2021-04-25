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
}
define quest_stages = {
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
