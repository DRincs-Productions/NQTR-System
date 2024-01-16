init python:
    def add_conversation_choice(choice_character, choice_text: str, label_name: str, dict_choices: dict[str, list] = None) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Conversation-system#add-an-talk-choice-in-default_label_talk """
        if not dict_choices:
            dict_choices = conversations
        if get_value_by_character_key(choice_character, dict_choices):
            dict_choices[choice_character].append((choice_text, label_name))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label_name))
            dict_choices[choice_character] = talk_choices
            del talk_choices
        return


    def del_conversation_choice(choice_character: str, choice_text: str, dict_choices: dict[str, list] = None) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Conversation-system#delete-an-action-in-default_label_talk """
        val = 0
        if not dict_choices:
            dict_choices = conversations
        ch_to_del = choice_character
        for cur_choice in get_value_by_character_key(choice_character, dict_choices):
            if cur_choice[0] == choice_text:
                ch_to_del = choice_character
                break
            else:
                val = val+1
        dict_choices[choice_character].pop(val)
        del val
        del ch_to_del
        return
