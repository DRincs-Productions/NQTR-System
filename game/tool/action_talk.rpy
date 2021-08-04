init -9 python:
    class TalkObject(object):
        """At the inside of the class there are the values used for the talk() function, 
        (all this could be done in Commitment(), but I preferred not to use a dictionary)"""
        def __init__(self,
            ch_secondary = [],
            bg_before_after=None,
            after_label_event=None,
            bg_talk=None,
            label_talk=None):

            self.ch_secondary = ch_secondary
            self.bg_before_after = bg_before_after
            self.bg_talk = bg_talk
            self.after_label_event = after_label_event
            self.label_talk = label_talk

        def talk(self):
            """Inside you can find the labels and images to start talk()"""
            # if label_talk == None does the default procedure
            if self.label_talk == None:
                renpy.jump('talk')
            else:
                renpy.jump(self.label_talk)

        def getTalkImage(self):
            """Returns the image during a conversation"""
            return self.bg_talk

        def getBeforeTalkImage(self):
            """Returns the background image used when someone is in the same room. It can be None"""
            return self.bg_before_after

        def getAfterTalkImage(self):
            """Returns the background image used after a conversation, 
            but if after_label_event is not null it passes to after_label_event. 
            ((the latter can be used in case the room is no longer accessible and thus takes you to another room))"""
            if self.after_label_event != None:
                renpy.jump(after_label_event)
            else:
                return self.bg_before_after

    def addTalkChoice(ch, choice_text, label):
        """Add the "choice" in the character's talkch_choices."""
        if (ch in talkch_choices.keys()):
            talkch_choices[ch].append((choice_text, label))
        else:
            talk_choices = []
            talk_choices.append((choice_text, label))
            talkch_choices[ch] = talk_choices
            del talk_choices
        return

    def delTalkChoice(ch, choice_text):
        """Deletes the "choice" in the character's talkch_choices."""
        val = 0
        for cur_choice in talkch_choices[ch]:
            if cur_choice[0] == choice_text:
                talkch_choices[ch].pop(val)
                del val
                return
            else:
                val = val+1
        del val
        return
