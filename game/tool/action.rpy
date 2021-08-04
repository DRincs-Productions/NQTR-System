init -9 python:
    class Action(object):
        """Actions of the MC"""
        def __init__(self,
            name,
            icon,
            label,
            icon_selected = None,
            sp_room = None,
            tm_start = 0,
            tm_stop = 25,
            day_start = None,
            day_deadline = None,
            is_in_room = False,
            xalign = 0,
            yalign = 0):
            # TODO: add the type as in routine
            # TODO: add the active value which is a value linked to bl_values, by default active = True

            self.name = name
            self.icon = icon
            self.label = label
            self.icon_selected = icon_selected
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.day_deadline = day_deadline
            self.day_start = day_start
            # it is used only in sp_actions
            self.sp_room = sp_room
            # Is an action that is started by clicking on an image in the room.
            self.is_in_room = is_in_room
            self.xalign = xalign
            self.yalign = yalign

    def getActions(room):
        """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)"""
        acts = []
        acts.clear()
        for act in sp_actions.values():
            if room.id == act.sp_room:
                if (tm.now_is_between(start=act.tm_start, end=act.tm_stop) and tm.day >= act.day_start):
                    acts.append(act)
        for act_id in room.id_actions:
            if act_id in df_actions:
                act = df_actions.get(act_id)
                if (tm.now_is_between(start=act.tm_start, end=act.tm_stop) and tm.day >= act.day_start):
                    acts.append(act)
                del act
        return acts

    def clearExpiredSPActions():
        """Delete Expired Actions"""
        alist = []
        alist.clear()
        for id, act in sp_actions.items():
            if (act.day_deadline != None and act.day_deadline <= tm.day):
                alist.append(id)
        for act_id in alist:
            alist.pop(act_id)
        del alist
        return

# TODO: Add a function that updates Actions after a load
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
