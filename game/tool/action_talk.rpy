define DEFAULT_LABEL_TALK = "talk"
define DEFAULT_TALK_BUTTON_ICON = "/interface/action-talk.webp"

init -11 python:
    class TalkObject(Button):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system """

        def __init__(self,
                    bg: str = None):

            self.bg = bg

        def isPictureInBackground(self):
            """This is a button?"""
            return button_icon != None

        def talk(self):
            """Inside you can find the labels and images to start talk()"""
            # if label_name == None does the default procedure
            if not isNullOrEmpty(self.label_name):
                renpy.jump(self.label_name)
            elif not isNullOrEmpty(DEFAULT_LABEL_TALK):
                renpy.jump(DEFAULT_LABEL_TALK)
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


    def addTalkChoice(choice_text: str, label_name: str, id_choice: str, dict_choices: dict[str, list]):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system#add-an-talk-choice """
        if (id_choice in dict_choices.keys()):
            dict_choices[id_choice].append((choice_text, label_name))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label_name))
            dict_choices[id_choice] = talk_choices
            del talk_choices
        return #talk_choices


    def delTalkChoice(choice_text: str, id_choice: str, dict_choices: dict[str, list]):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system#delete-an-action """
        val = 0
        ch_to_del = id_choice
        for cur_choice in dict_choices[id_choice]:
            if cur_choice[0] == choice_text:
                ch_to_del = id_choice
                break
            else:
                val = val+1
        dict_choices[id_choice].pop(val)
        del val
        del ch_to_del
        return #dict_choices
