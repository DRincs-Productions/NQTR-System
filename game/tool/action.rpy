init -5 python:
    class Action(Button):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action """

        def __init__(self,
                    rooms: list[str] = [],
                    tm_start: int = 0,
                    tm_stop: int = 25,
                    day_start: int = -1,
                    day_deadline: int = -1):
            # TODO: add the type as in routine

            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.day_deadline = day_deadline
            self.day_start = day_start
            self.rooms = rooms
            if self.day_start < 0:
                renpy.log("Warn: You have set day_start < 0, so it will be ignored")
            if self.day_deadline < 0:
                renpy.log(
                    "Warn: You have set day_deadline < 0, so it will be ignored")


    def getActions(actions: dict[str, Action], room: Room,  tm: TimeHandler):
        """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)"""
        acts: list[Action] = []
        for act_id, act in actions.items():
            if room.id in act.rooms:
                if (tm.now_is_between(start=act.tm_start, end=act.tm_stop) and (act.day_start < 0 | tm.day >= act.day_start)):
                    acts.append(act)
            elif act_id in room.id_actions:
                if (tm.now_is_between(start=act.tm_start, end=act.tm_stop) and (act.day_start < 0 | tm.day >= act.day_start)):
                    acts.append(act)
        return acts


    def clearExpiredActions(actions: dict[str, Action], tm: TimeHandler):
        """Delete Expired Actions"""
        actions_to_del = []
        for id, act in actions.items():
            if (act.day_deadline and act.day_deadline <= tm.day):
                actions_to_del.append(id)
        for act_id in actions_to_del:
            del actions[act_id]
        del actions_to_del
        return actions

# TODO: Add a function that updates Actions after a load
