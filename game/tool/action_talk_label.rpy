define talk_ch = None
default talk_image = None
# used in talk_menu, internally there are the possible choices that you can make in a dialog with a certain ch
# is structured like this:
# 'alice'   :   [("Choice 1", "label_one"), ("Choice 2", "label_two")]
default talkch_choices = {}

# Opens the choice menu, with the various dialogs you can currently do with a ch
label talk_menu:
    # check if there is already a list of menu choices for talk_ch
    # if it does not exist it creates it
    if (talk_ch in talkch_choices.keys()):
        $ talk_choices = talkch_choices[talk_ch]
    else:
        $ talk_choices = []

    $ talk_choices.append((_("Back"), "talk_back"))
    $ menu_result = menu(talk_choices)
    # remove the item because otherwise every time I talk to a character more "Back" will be added (even if I have not understood why)
    $ talk_choices.remove((_("Back"), "talk_back"))
    $ del talk_choices
    call expression menu_result
    return

# label talk: is a label used to give the possibility to customize the dialog even more.
label talk:
    if (talk_image != None):
        scene expression (talk_image) as bg

    if(talk_ch == None):
        call log_error("talk_ch is None", renpy.get_filename_line())
        return

    # Costume Code
    if(talk_ch == "alice"):
        mc "Hi [a]"
        a "Hi, can you tell me something?"
    else:
        "Now is busy test later."

    call talk_menu
    return

# Display a random phrase and then end the conversation
label talk_back:
    $ num = renpy.random.randint(1, 7)
    if num == 1:
        mc "OK, I'm off. See you."
    elif num == 2:
        mc "It's getting late. See you."
    elif num == 3:
        mc "Sorry, but I have to go now. Bye."
    elif num == 4:
        mc "Good talk. We should do this more often."
    elif num == 5:
        mc "I just remembered something. Gotta go! Bye."
    elif num == 6:
        mc "I won't keep you any longer. Bye."
    elif num == 7:
        mc "I was supposed to tell you something else.... But I can't remember."
        mc "When it comes back to me I'll let you know, bye."

    $ del num
    return

# Quest "alice"

label stage_talkalice:
    if (number_stages_completed_in_quest["alice"] == 0):
        show bg alice terrace talk
        a "Hi can you order me a new book from pc?"
        mc "Ok"
        a "Thanks"

        $ addTalkChoice(choice_id = "alice", choice_text = _("About the book"), label_name = "stage_talkalice", dict_choices = talkch_choices)

        $ actions["order_product"] = Act(name = _("Order product"),  button_icon = "/interface/action-pc.webp", label_name = "order_product", rooms=["my_room"])

        $ quests["alice"].nextStage()
    elif (number_stages_completed_in_quest["alice"] == 1):
        mc "What book do you want me to order?"
        a "For me it is the same."
        jump talk_menu
    elif (number_stages_completed_in_quest["alice"] == 2):
        mc "I ordered the Book, hope you enjoy it."
        a "Great, when it arrives remember to bring it to me."
        jump talk_menu
    elif (number_stages_completed_in_quest["alice"] == 3):
        mc "Here's your book."
        a "Thank you, I can finally read something new."
        $ quests["alice"].nextStage()
        $ delTalkChoice(choice_id = "alice", choice_text = _("About the book"), dict_choices = talkch_choices)
    return

# Quest "ann"

label stage_talkalice_aboutann:
    show bg alice terrace talk
    mc "Alice, I was thinking of visiting Ann. can you lend me your car?"
    a "Yes, of course. You can find the keys on the keyhole in the hall."
    mc "Thanks!"
    a "Don't ruin it..."
    $ actions["take_key"] = Act(name = _("KEY"),  picture_in_background = "/action-key.webp", label_name = "take_key", rooms=['lounge'],
        xalign = 608, yalign = 667)

    $ quests["ann"].nextStage()
    $ delTalkChoice(choice_id = "alice", choice_text = _("About the Ann"), dict_choices = talkch_choices)
    return
