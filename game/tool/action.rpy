init -5 python:
    class Action:
        """Actions of the MC,
        day_deadline & day_start must be >0, if not the value will be ignored"""

        def __init__(self,
                    name: str,
                    label_name: str,
                    icon_selected: str = None,
                    room: str = None,
                    tm_start: int = 0,
                    tm_stop: int = 25,
                    day_start: int = -1,
                    day_deadline: int = -1,
                    button_icon: str = None,
                    picture_in_background: str = None,
                    xpos: int = None,
                    ypos: int = None):
            # TODO: add the type as in routine
            # TODO: add the active value which is a value linked to flags, by default active = True

            self.name = name
            self.button_icon = button_icon
            self.label_name = label_name
            self.icon_selected = icon_selected
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.day_deadline = day_deadline
            self.day_start = day_start
            self.room = room
            # Is an action that is started by clicking on an image in the room.
            self.picture_in_background = picture_in_background
            self.xpos = xpos
            self.ypos = ypos
            if self.day_start < 0:
                renpy.log("Warn: You have set day_start < 0, so it will be ignored")
            if self.day_deadline < 0:
                renpy.log(
                    "Warn: You have set day_deadline < 0, so it will be ignored")
            if (self.xpos != None and self.ypos == None):
                renpy.log(
                    "Warn: xpos is set but ypos is not, so ypos set to 0")
                self.ypos = 0
            if (self.xpos == None and self.ypos != None):
                renpy.log(
                    "Warn: ypos is set but xpos is not, so xpos set to 0")
                self.xpos = 0
            if (self.button_icon == None and self.picture_in_background == None):
                renpy.log(
                    "Error: You have set button_icon and picture_in_background to None, this action will be ignored")

        def isButton(self):
            """This is a button?"""
            return self.button_icon != None

        def isPictureInBackground(self):
            """This is a button?"""
            return self.button_icon != None


    def getActions(actions: dict[str, Action], room: Room,  tm: TimeHandler):
        """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)"""
        acts: list[Action] = []
        for act_id, act in actions.items():
            if room.id == act.room:
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
