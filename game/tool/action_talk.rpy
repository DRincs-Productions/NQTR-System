define DEFAULT_LABEL_TALK = "talk"
define DEFAULT_TALK_BUTTON_ICON = "/interface/action-talk.webp"

init -11 python:
    class TalkObject(Button):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system """

        def __init__(self,
                    # only TalkObject
                    bg: str = None,
                    # Button
                    name: str = None,
                    label_name: str = None,
                    button_icon: str = None,
                    button_icon_selected: str = None,
                    picture_in_background: str = None,
                    picture_in_background_selected: str = None,
                    xpos: int = None,
                    ypos: int = None,
                    ):
            super().__init__(
                name= name,
                label_name= label_name,
                button_icon= button_icon,
                button_icon_selected= button_icon_selected,
                picture_in_background= picture_in_background,
                picture_in_background_selected= picture_in_background_selected,
                xpos= xpos,
                ypos= ypos,
            )

            self.bg = bg

        def isPictureInBackground(self):
            """This is a button?"""
            return button_icon != None

        def talk(self):
            """Inside you can find the labels and images to start talk()"""
            # if label_name == None does the default procedure
            if not isNullOrEmpty(self.label_name):
                renpy.call(self.label_name)
            elif not isNullOrEmpty(DEFAULT_LABEL_TALK):
                renpy.call(DEFAULT_LABEL_TALK)
            return

        def getBackground(self):
            """Returns the image during a conversation"""
            return self.bg

        def getButtonIcon(self):
            if(self.button_icon != None):
                return button_icon
            else:
                return DEFAULT_TALK_BUTTON_ICON
            return self.bg


    def addTalkChoice(choice_text: str, label_name: str, choice_id: str, dict_choices: dict[str, list]):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system#add-an-talk-choice-in-default_label_talk """
        if (choice_id in dict_choices.keys()):
            dict_choices[choice_id].append((choice_text, label_name))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label_name))
            dict_choices[choice_id] = talk_choices
            del talk_choices
        return #talk_choices


    def delTalkChoice(choice_text: str, choice_id: str, dict_choices: dict[str, list]):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system#delete-an-action-in-default_label_talk """
        val = 0
        ch_to_del = choice_id
        for cur_choice in dict_choices[choice_id]:
            if cur_choice[0] == choice_text:
                ch_to_del = choice_id
                break
            else:
                val = val+1
        dict_choices[choice_id].pop(val)
        del val
        del ch_to_del
        return #dict_choices
