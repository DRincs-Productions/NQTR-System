init python:
    def addTalkChoice(choice_text: str, label_name: str, choice_id: str, dict_choices: dict[str, list]) -> None:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system#add-an-talk-choice-in-default_label_talk """
        if (choice_id in dict_choices.keys()):
            dict_choices[choice_id].append((choice_text, label_name))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label_name))
            dict_choices[choice_id] = talk_choices
            del talk_choices
        return
