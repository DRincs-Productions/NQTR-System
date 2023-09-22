init python:
    def add_conversation_choice(choice_character, choice_text: str, label_name: str, dict_choices: dict[str, list]) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system#add-an-talk-choice-in-default_label_talk """
        if (choice_character in dict_choices.keys()):
            dict_choices[choice_character].append((choice_text, label_name))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label_name))
            dict_choices[choice_character] = talk_choices
            del talk_choices
        return


    def del_conversation_choice(choice_text: str, choice_character: str, dict_choices: dict[str, list]) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system#delete-an-action-in-default_label_talk """
        val = 0
        ch_to_del = choice_character
        for cur_choice in dict_choices[choice_character]:
            if cur_choice[0] == choice_text:
                ch_to_del = choice_character
                break
            else:
                val = val+1
        dict_choices[choice_character].pop(val)
        del val
        del ch_to_del
        return
