define DEFAULT_LABEL_TALK = "talk"

init -11 python:
    class TalkObject:
        """At the inside of the class there are the values used for the talk() function, 
        (all this could be done in Commitment(), but I preferred not to use a dictionary)"""

        def __init__(self,
                    bg: str = None,
                    label_name: str = None):

            self.bg = bg
            self.label_name = label_name

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


    def addTalkChoice(choice_text: str, label_name: str, id_choice: str, dict_choices: dict[str, list]):
        """Add the "choice" in the character's dict_choices."""
        if (id_choice in dict_choices.keys()):
            dict_choices[id_choice].append((choice_text, label_name))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label_name))
            dict_choices[id_choice] = talk_choices
            del talk_choices
        return #talk_choices


    def delTalkChoice(choice_text: str, id_choice: str, dict_choices: dict[str, list]):
        """Deletes the "choice" in the character's dict_choices."""
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
