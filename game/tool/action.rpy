init -5 python:
    class Action(object):
        """Actions of the MC,
        day_deadline & day_start must be >0, if not the value will be ignored"""

        def __init__(self,
                    name: str,
                    icon: str,
                    label: str,
                    icon_selected: str = None,
                    room: str = None,
                    tm_start: int = 0,
                    tm_stop: int = 25,
                    day_start: int = -1,
                    day_deadline: int = -1,
                    is_in_room: bool = False,
                    xpos: int = 0,
                    ypos: int = 0):
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
            self.room = room
            # Is an action that is started by clicking on an image in the room.
            self.is_in_room = is_in_room
            self.xpos = xpos
            self.ypos = ypos
            if self.day_start < 0:
                renpy.log("Warn: You have set day_start < 0, so it will be ignored")
            if self.day_deadline < 0:
                renpy.log(
                    "Warn: You have set day_deadline < 0, so it will be ignored")


    def getActions(actions: dict[str, Action], room: Room,  tm: TimeHandler):
        """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)"""
        acts: list[Action] = []
        acts.clear()
        for act_id in actions.keys():
            act = actions[act_id]
            if room.id == act.room:
                if (tm.now_is_between(start=act.tm_start, end=act.tm_stop) and (act.day_start < 0 | tm.day >= act.day_start)):
                    acts.append(act)
            elif act_id in room.id_actions:
                if (tm.now_is_between(start=act.tm_start, end=act.tm_stop) and (act.day_start < 0 | tm.day >= act.day_start)):
                    acts.append(act)
            del act
        return acts


    def clearExpiredSPActions(sp_actions: dict[str, Action], tm: TimeHandler):
        """Delete Expired Actions"""
        alist = []
        alist.clear()
        for id, act in sp_actions.items():
            if (act.day_deadline and act.day_deadline <= tm.day):
                alist.append(id)
        for act_id in alist:
            sp_actions.pop(act_id)
        del alist
        return sp_actions

# TODO: Add a function that updates Actions after a load
