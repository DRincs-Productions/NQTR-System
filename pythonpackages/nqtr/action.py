from typing import Optional, Union

from pythonpackages.nqtr.button import Button
from pythonpackages.nqtr.navigation import Room
from pythonpackages.nqtr.time import TimeHandler
from pythonpackages.renpy_custom_log import *


class Act(Button):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action """

    def __init__(
        self,
        # Requirement
        name: str,
        label_name: str,
        # Act params
        rooms: Optional[list[str]] = None,
        tm_start: int = 0,
        tm_stop: int = 25,
        day_start: int = -1,
        day_deadline: int = -1,
        # Button params
        button_icon: str = None,
        button_icon_selected: str = None,
        picture_in_background: str = None,
        picture_in_background_selected: str = None,
        xalign: int = None,
        yalign: int = None,
        disabled: Union[bool, str] = False,
        hidden: Union[bool, str] = False,
    ):

        # Button init
        super().__init__(
            name=name,
            label_name=label_name,
            button_icon=button_icon,
            button_icon_selected=button_icon_selected,
            picture_in_background=picture_in_background,
            picture_in_background_selected=picture_in_background_selected,
            xalign=xalign,
            yalign=yalign,
            disabled=disabled,
            hidden=hidden,
        )
        # Act init
        self.tm_start = tm_start
        self.tm_stop = tm_stop-0.1
        self.day_deadline = day_deadline
        self.day_start = day_start
        self.rooms = rooms if rooms else []
        if self.day_start < 0:
            log_info("You have set day_start < 0, so it will be ignored",
                     "nqtr.action.Act.__init__")
        if self.day_deadline < 0:
            log_info("You have set day_deadline < 0, so it will be ignored",
                     "nqtr.action.Act.__init__")


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


def getActions(actions: dict[str, Act], room: Room, now_hour: int, cur_day: int, tm: TimeHandler) -> list[Act]:
    """Return all possible actions in a certain room (ATTENTION: give a Room object as parameter, and not the id)"""
    acts: list[Act] = []
    for act_id, act in actions.items():
        if room.id in act.rooms:
            if (tm.now_is_between(start=act.tm_start, end=act.tm_stop, now=now_hour) and (act.day_start < 0 | cur_day >= act.day_start)):
                acts.append(act)
        elif act_id in room.action_ids:
            if (tm.now_is_between(start=act.tm_start, end=act.tm_stop, now=now_hour) and (act.day_start < 0 | cur_day >= act.day_start)):
                acts.append(act)
    return acts
