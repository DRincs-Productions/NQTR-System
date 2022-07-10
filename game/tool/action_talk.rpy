define DEFAULT_LABEL_TALK = "talk"

init -11 python:
    class TalkObject:
        """At the inside of the class there are the values used for the talk() function, 
        (all this could be done in Commitment(), but I preferred not to use a dictionary)"""

        def __init__(self,
                    bg: str  = None,
                    label_name: str  = None):

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


    def addTalkChoice(ch: str, choice_text: str, label: str, talkch_choices: dict[str, list]): # TODO: add a type for list
        """Add the "choice" in the character's talkch_choices."""
        if (ch in talkch_choices.keys()):
            talkch_choices[ch].append((choice_text, label))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label))
            talkch_choices[ch] = talk_choices
            del talk_choices
        return


    def delTalkChoice(ch: str, choice_text: str, talkch_choices: dict[str, list]): # TODO: add a type for list
        """Deletes the "choice" in the character's talkch_choices."""
        val = 0
        ch_to_del = ch
        for cur_choice in talkch_choices[ch]:
            if cur_choice[0] == choice_text:
                ch_to_del = ch
                break
            else:
                val = val+1
        talkch_choices[ch].pop(val)
        del val
        del ch_to_del
        return
