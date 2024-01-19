# Display a random phrase and then end the conversation
label talk_back_custom:
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

        $ add_conversation_choice(choice_character = a, choice_text = _("About the book"), label_name = "stage_talkalice")

        $ actions["order_product"] = Act(name = _("Order product"),  button_icon = "action pc", label_name = "order_product", room_ids=["my_room"])

        $ quest_next_stage(id = "alice")
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
        $ quest_next_stage(id = "alice")
        $ del_conversation_choice(choice_character = a, choice_text = _("About the book"))
    return

# Quest "ann"

label stage_talkalice_aboutann:
    show bg alice terrace talk
    mc "Alice, I was thinking of visiting Ann. can you lend me your car?"
    a "Yes, of course. You can find the keys on the keyhole in the hall."
    mc "Thanks!"
    a "Don't ruin it..."
    $ actions["take_key"] = Act(name = _("KEY"),  picture_in_background = "/action-key.webp", label_name = "take_key", room_ids=['lounge'],
        xalign = 608/1920, yalign = 667/1080)

    $ quest_next_stage(id = "ann")
    $ del_conversation_choice(choice_character = a, choice_text = _("About the Ann"))
    return
