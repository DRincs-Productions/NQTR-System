init -9 python:
    class Action(object):
        """Actions of the MC"""
        def __init__(self, name, icon, label, sp_room=None, tm_start=0, tm_stop=25, day_start=None, day_deadline=None):
            self.name = name
            self.icon = icon
            self.label = label
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.day_deadline = day_deadline
            self.day_start = day_start
            # it is used only in sp_actions
            self.sp_room = sp_room

    def getActions(room):
        """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)"""
        acts = []
        acts.clear()
        for act in sp_actions.values():
            if room.id == act.sp_room:
                if (tm.now_is_between(act.tm_start, act.tm_stop) and tm.day >= act.day_start):
                    acts.append(act)
        for act_id in room.actions:
            if act_id in df_actions:
                act = df_actions.get(act_id)
                if (tm.now_is_between(act.tm_start, act.tm_stop) and tm.day >= act.day_start):
                    acts.append(act)
                del act
        return acts

    def clearExpiredSPActions():
        """Delete Expired Actions"""
        alist = []
        alist.clear()
        for act in sp_actions.values():
            if (act.day_deadline != None and act.day_deadline <= tm.day):
                alist.append(act)
        for act in alist:
            alist.pop(act)
        del alist
        return
