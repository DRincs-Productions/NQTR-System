init -5 python:
    from typing import Optional


    class Act:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action """

        def __init__(self,
                    name: str,  # requirement
                    label_name: str,  # requirement
                    rooms: Optional[list[str]] = None,
                    tm_start: int = 0,
                    tm_stop: int = 25,
                    day_start: int = -1,
                    day_deadline: int = -1,
                    button_icon: str = None,
                    button_icon_selected: str = None,
                    picture_in_background: str = None,
                    picture_in_background_selected: str = None,
                    xpos: int = None,
                    ypos: int = None):

            self.name = name
            self.label_name = label_name
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.day_deadline = day_deadline
            self.day_start = day_start
            self.rooms = rooms if rooms else []
            self.button_icon = button_icon
            self.button_icon_selected = button_icon_selected
            # Is an action that is started by clicking on an image in the room.
            self.picture_in_background = picture_in_background
            self.picture_in_background_selected = picture_in_background_selected
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
            if (isNullOrEmpty(self.button_icon) and isNullOrEmpty(self.picture_in_background)):
                renpy.log(
                    "Error: You have set button_icon and picture_in_background to None, this action will be ignored")

        def isButton(self) -> bool:
            """This is a button?"""
            return not isNullOrEmpty(self.button_icon)

        def isPictureInBackground(self) -> bool:
            """This is a is picture in background?"""
            return not isNullOrEmpty(self.picture_in_background)


    def getActions(actions: dict[str, Act], room: Room,  now_is_between: callable[[int, int], bool], cur_day: int) -> list[Act]:
        """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)
        now_is_between: (tm_start, tm_stop) -> bool"""
        acts: list[Act] = []
        for act_id, act in actions.items():
            if room.id in act.rooms:
                if (now_is_between(start=act.tm_start, end=act.tm_stop) and (act.day_start < 0 | cur_day >= act.day_start)):
                    acts.append(act)
            elif act_id in room.action_ids:
                if (now_is_between(start=act.tm_start, end=act.tm_stop) and (act.day_start < 0 | cur_day >= act.day_start)):
                    acts.append(act)
        return acts


    def clearExpiredActions(actions: dict[str, Act], cur_day: int) -> None:
        """Delete Expired Actions"""
        actions_to_del = []
        for id, act in actions.items():
            if (act.day_deadline and act.day_deadline <= cur_day):
                actions_to_del.append(id)
        for act_id in actions_to_del:
            del actions[act_id]
        del actions_to_del
        return
