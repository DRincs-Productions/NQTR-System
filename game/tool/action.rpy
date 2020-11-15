init -9 python:
    class Action(object):
        """Actions of the MC"""
        def __init__(self, id, name, icon, label = 'error_label', sp_room='', tm_start=0, tm_stop=24):
            self.id = id
            self.name = name
            self.icon = icon
            self.label = label
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            # it is used only in sp_actions
            self.sp_room = sp_room

    def getActions(room):
        """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)"""
        acts = []
        for act in actions:
            for act_id in room.actions:
                if act.id == act_id:
                    if (tm.now_is_between(act.tm_start, act.tm_stop)):
                        acts.append(act)
        for act in sp_actions:
            if room.id == act.sp_room:
                if (tm.now_is_between(act.tm_start, act.tm_stop)):
                    acts.append(act)
        return acts

# habitual actions
define actions = [
        Action("nap", _("Nap"), "/interface/action-sleep.webp", label = "nap", tm_start=5, tm_stop=23), 
        Action("sleep", _("Sleep"), "/interface/action-alarm.webp", label = "sleep", tm_start=23, tm_stop=5), 
    ]
# "special" actions:
# they are not usual actions, but actions inserted and removed for a specific reason, for example for a quest.
# IMPORTANT: specify in sp_room the id of the room where the action will take place
default sp_actions = [
    ]
