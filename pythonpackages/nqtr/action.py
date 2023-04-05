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
        day_start: Optional[int] = None,
        day_deadline: Optional[int] = None,
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
        if self.day_start is int and self.day_start < 0:
            self.day_start = None
            log_info("You have set day_start < 0, so it will be ignored",
                     "nqtr.action.Act.__init__")
        if self.day_deadline is int and self.day_deadline < 0:
            self.day_deadline = None
            log_info("You have set day_deadline < 0, so it will be ignored",
                     "nqtr.action.Act.__init__")

    def is_deadline(self, current_day: int) -> bool:
        """Return True if the deadline is passed"""
        if self.day_deadline and self.day_deadline <= current_day:
            return True
        return False

    def have_valid_day(self, current_day: int) -> bool:
        """Return True if the action is valid for the current day"""
        if self.day_start and self.day_start >= current_day:
            return False
        return not self.is_deadline(current_day)


def clearExpiredActions(actions: dict[str, Act], current_day: int) -> None:
    """Delete Expired Actions"""
    actions_to_del = []
    for id, act in actions.items():
        if (act.is_deadline(current_day)):
            actions_to_del.append(id)
    for act_id in actions_to_del:
        del actions[act_id]
    del actions_to_del
    return


def getActions(actions: dict[str, Act], room: Room, now_hour: int, current_day: int, tm: TimeHandler) -> list[Act]:
    """Return a action list for the current room and available for the current time""""
    acts: list[Act] = []
    for act_id, act in actions.items():
        if room.id in act.rooms or act_id in room.action_ids:
            if act.have_valid_day(current_day) and tm.now_is_between(start=act.tm_start, end=act.tm_stop, now=now_hour):
                acts.append(act)
    return acts
