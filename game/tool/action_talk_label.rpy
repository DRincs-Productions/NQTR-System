define talk_ch = None
default talk_image = None
default talk_end_image = None
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
    jump expression menu_result
    return

# Best way to exit a dialogue
label talk_end:
    if (talk_end_image != None):
        scene expression (talk_end_image) as bg

    call screen room_navigation

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
        mc "I was supposed to tell you something else.... But I don't remember."
        mc "Patience when it comes back to me I'll let you know, bye."

    $ del num
    jump talk_end

# Quest "alice"

label stage_talkalice:
    if (quests_levels["alice"] == 0):
        show bg alice terrace talk
        a "Hi can you order me a new book from pc?"
        mc "Ok"
        a "Thanks"

        $ addTalkChoice(ch = "alice", choice_text = _("About the book"), label = "stage_talkalice")

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
        $ delTalkChoice(ch = "alice", choice_text = _("About the book"))
    return

# Quest "ann"

label stage_talkalice_aboutann:
    show bg alice terrace talk
    mc "Alice, I was thinking of visiting Ann. can you lend me your car?"
    a "Yes, of course. You can find the keys on the keyhole in the hall."
    mc "Thanks!"
    a "Don't ruin it..."
    $ sp_actions["take_key"] = Action(_("KEY"), "/action-key.webp", label = "take_key", sp_room='lounge',
        is_in_room = True, xpos = 608, ypos = 667)

    $ quests["ann"].next_stage()
    $ delTalkChoice(ch = "alice", choice_text = _("About the Ann"))
    return
