init -9 python:
    class Action(object):
        """Actions of the MC"""
        def __init__(self, id, name, icon, label, sp_room=None, tm_start=0, tm_stop=25, day_start=None, day_deadline=None):
            self.id = id
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
        for act in actions:
            for act_id in room.actions:
                if act.id == act_id:
                    if (tm.now_is_between(act.tm_start, act.tm_stop) and tm.day >= act.day_start):
                        acts.append(act)
        for act in sp_actions:
            if room.id == act.sp_room:
                if (tm.now_is_between(act.tm_start, act.tm_stop) and tm.day >= act.day_start):
                    acts.append(act)
        return acts

    def removeSpAction(act_id):
        for act in sp_actions:
            if act.id == act_id:
                sp_actions.remove(act)
        return

    def clearExpiredSPActions():
        """Delete Expired Actions"""
        alist = []
        alist.clear()
        for a in sp_actions:
            if (a.day_deadline != None and a.day_deadline <= tm.day):
                alist.append(a)
        for a in alist:
            sp_actions.remove(a)
        del alist
        return
