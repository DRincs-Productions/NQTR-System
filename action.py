from typing import Optional, Union

from pythonpackages.nqtr.button import Button
from pythonpackages.nqtr.navigation import Room
from pythonpackages.nqtr.time import MAX_DAY_HOUR, TimeHandler
from pythonpackages.renpy_utility.renpy_custom_log import *


class Act(Button):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action"""

    def __init__(
        self,
        # Requirement Button params
        name: str,
        label_name: str,
        # Act params
        room_ids: list[str] = [],
        hour_start: int = 0,
        hour_stop: Union[int, float] = MAX_DAY_HOUR + 1,
        day_start: Optional[int] = None,
        day_deadline: Optional[int] = None,
        # Button params
        button_icon: Optional[str] = None,
        button_icon_selected: Optional[str] = None,
        picture_in_background: Optional[str] = None,
        picture_in_background_selected: Optional[str] = None,
        xalign: Optional[int] = None,
        yalign: Optional[int] = None,
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
        self.hour_start = hour_start
        self.hour_stop = hour_stop - 0.1
        self.day_deadline = day_deadline
        self.day_start = day_start
        self.room_ids = room_ids
        if isinstance(self.day_start, int) and self.day_start < 0:
            self.day_start = None
            log_info(
                "You have set day_start < 0, so it will be ignored",
                "nqtr.action.Act.__init__",
            )
        if isinstance(self.day_deadline, int) and self.day_deadline < 0:
            self.day_deadline = None
            log_info(
                "You have set day_deadline < 0, so it will be ignored",
                "nqtr.action.Act.__init__",
            )

    @property
    def room_ids(self) -> list[str]:
        """List of room ids where this act can be done"""
        return self._room_ids

    @room_ids.setter
    def room_ids(self, value: list[str]):
        self._room_ids = value

    @property
    def rooms(self) -> list[str]:
        """Deprecated, use room_ids"""
        return self._room_ids

    @rooms.setter
    def rooms(self, value: Optional[list[str]]):
        """Deprecated, use room_ids"""
        self._room_ids = value if value else []

    @property
    def hour_start(self) -> int:
        """Start hour of the action"""
        return self._hour_start

    @hour_start.setter
    def hour_start(self, value: int):
        self._hour_start = value

    @property
    def hour_stop(self) -> Union[int, float]:
        """Stop hour of the action"""
        return self._hour_stop

    @hour_stop.setter
    def hour_stop(self, value: Union[int, float]):
        self._hour_stop = value

    @property
    def day_start(self) -> Optional[int]:
        """Start day of the action"""
        return self._day_start

    @day_start.setter
    def day_start(self, value: Optional[int]):
        self._day_start = value

    @property
    def day_deadline(self) -> Optional[int]:
        """Deadline day of the action"""
        return self._day_deadline

    @day_deadline.setter
    def day_deadline(self, value: Optional[int]):
        self._day_deadline = value

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


def clear_expired_actions(actions: dict[str, Act], current_day: int) -> None:
    """Delete Expired Actions"""
    actions_to_del = []
    for id, act in actions.items():
        if act.is_deadline(current_day):
            actions_to_del.append(id)
    for act_id in actions_to_del:
        del actions[act_id]
    del actions_to_del
    return


def current_actions(
    actions: dict[str, Act],
    room: Room,
    now_hour: int,
    current_day: int,
    tm: TimeHandler,
    flags: dict[str, bool] = {},
) -> list[Act]:
    """Return a action list for the current room and available for the current time"""
    acts: list[Act] = []
    for act_id, act in actions.items():
        if not act.is_hidden(flags):
            if is_action_in_current_room(act_id, act, room, now_hour, current_day, tm):
                acts.append(act)
    return acts


def is_action_in_current_room(
    act_id: str,
    action: Act,
    room: Room,
    now_hour: int,
    current_day: int,
    tm: TimeHandler,
) -> bool:
    """Return True if the action is in the current room and available for the current time"""
    if room.id in action.room_ids or act_id in room.action_ids:
        if action.have_valid_day(current_day) and tm.now_is_between(
            start=action.hour_start, end=action.hour_stop, now=now_hour
        ):
            return True
    return False


def current_button_actions(
    actions: dict[str, Act],
    room: Room,
    now_hour: int,
    current_day: int,
    tm: TimeHandler,
    flags: dict[str, bool] = {},
) -> list[Act]:
    """Return a button action list for the current room and available for the current time"""
    acts: list[Act] = []
    for act_id, act in actions.items():
        if act.is_button and not act.is_hidden(flags):
            if is_action_in_current_room(act_id, act, room, now_hour, current_day, tm):
                acts.append(act)
    return acts


def current_picture_in_background_actions(
    actions: dict[str, Act],
    room: Room,
    now_hour: int,
    current_day: int,
    tm: TimeHandler,
    flags: dict[str, bool] = {},
) -> list[Act]:
    """Return a picture in background action list for the current room and available for the current time"""
    acts: list[Act] = []
    for act_id, act in actions.items():
        if act.is_picture_in_background and not act.is_hidden(flags):
            if is_action_in_current_room(act_id, act, room, now_hour, current_day, tm):
                acts.append(act)
    return acts
