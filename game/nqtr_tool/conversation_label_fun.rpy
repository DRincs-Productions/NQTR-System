define current_conversation_character = None
default conversation_image = None
# used in talk_menu, internally there are the possible choices that you can make in a dialog with a certain ch
# is structured like this:
# 'alice'   :   [("Choice 1", "label_one"), ("Choice 2", "label_two")]
default conversations = {}

# Opens the choice menu, with the various dialogs you can currently do with a ch
label talk_menu:
    # check if there is already a list of menu choices for current_conversation_character
    # if it does not exist it creates it
    $ talk_choices = get_value_by_character_key(current_conversation_character, conversations)
    if not talk_choices:
        $ talk_choices = []

    $ talk_choices.append((_("Back"), "talk_back"))
    $ menu_result = menu(talk_choices)
    # remove the item because otherwise every time I talk to a character more "Back" will be added (even if I have not understood why)
    $ talk_choices.remove((_("Back"), "talk_back"))
    $ del talk_choices
    call expression menu_result
    return

# label nqtr_talk: is a label used to give the possibility to customize the dialog even more.
label nqtr_talk:
    if (conversation_image != None):
        scene expression (conversation_image) as bg

    if(current_conversation_character == None):
        $ log_error("current_conversation_character is None", renpy.get_filename_line())
        return

    call talk_menu
    return

# Display a random phrase and then end the conversation
label talk_back:
    if renpy.has_label("talk_back_custom"):
        call talk_back_custom
    return
