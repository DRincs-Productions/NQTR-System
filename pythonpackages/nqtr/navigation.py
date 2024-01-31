from typing import Optional, Union

from pythonpackages.nqtr.button import Button
from pythonpackages.nqtr.routine import Commitment
from pythonpackages.nqtr.time import TimeHandler
from pythonpackages.renpy_utility.renpy_custom_log import *


class Room(Button):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room"""

    def __init__(
        self,
        # Requirement Button params
        name: str,
        # Requirement
        id: str,
        location_id: str,
        # Room params
        background: Optional[str] = None,
        action_ids: list[str] = [],
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
            button_icon=button_icon,
            button_icon_selected=button_icon_selected,
            picture_in_background=picture_in_background,
            picture_in_background_selected=picture_in_background_selected,
            xalign=xalign,
            yalign=yalign,
            disabled=disabled,
            hidden=hidden,
        )
        # Room init
        self.id = id
        self.location_id = location_id
        self.background = background
        self.action_ids = action_ids

    @property
    def id(self) -> str:
        """Room id"""
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def location_id(self) -> str:
        """Location id where the Room is located"""
        return self._location_id

    @location_id.setter
    def location_id(self, value: str):
        self._location_id = value

    @property
    def background(self) -> Optional[str]:
        """Image path shown when standing at the Room"""
        return self._bg

    @background.setter
    def background(self, value: Optional[str]):
        self._bg = value

    @property
    def action_ids(self) -> list[str]:
        """List of action ids that can be performed in the Room"""
        return self._action_ids

    @action_ids.setter
    def action_ids(self, value: list[str]):
        self._action_ids = value


class Location(Button):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location"""

    def __init__(
        self,
        # Requirement
        id: str,
        map_id: str,
        external_room_id: str,
        # Requirement Button params
        name: str,
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
            button_icon=button_icon,
            button_icon_selected=button_icon_selected,
            picture_in_background=picture_in_background,
            picture_in_background_selected=picture_in_background_selected,
            xalign=xalign,
            yalign=yalign,
            disabled=disabled,
            hidden=hidden,
        )
        self.id = id
        self.map_id = map_id
        self.external_room_id = external_room_id

    @property
    def id(self) -> str:
        """Location id"""
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value

    @property
    def map_id(self) -> str:
        """Map id where the Location is located"""
        return self._map_id

    @map_id.setter
    def map_id(self, value: str):
        self._map_id = value

    @property
    def external_room_id(self) -> str:
        """Room id where the Location is located.
        Will be set this room when a location is changed"""
        return self._external_room_id

    @external_room_id.setter
    def external_room_id(self, value: str):
        self._external_room_id = value


class Map(Button):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map"""

    def __init__(
        self,
        # Requirement Button params
        name: str,
        # Map params
        background: str,
        map_id_north: Optional[str] = None,
        map_id_south: Optional[str] = None,
        map_id_west: Optional[str] = None,
        map_id_east: Optional[str] = None,
        # Button params
        disabled: Union[bool, str] = False,
        hidden: Union[bool, str] = False,
    ):
        # Button init
        super().__init__(
            name=name,
            button_icon=None,
            button_icon_selected=None,
            picture_in_background=None,
            picture_in_background_selected=None,
            xalign=None,
            yalign=None,
            disabled=disabled,
            hidden=hidden,
        )
        self.background = background
        self.map_id_north = map_id_north
        self.map_id_south = map_id_south
        self.map_id_west = map_id_west
        self.map_id_east = map_id_east

    @property
    def background(self) -> str:
        """Image path shown when standing at the Map"""
        return self._bg

    @background.setter
    def background(self, value: str):
        self._bg = value

    @property
    def map_id_north(self) -> Optional[str]:
        """Map id where the Map is located"""
        return self._map_id_north

    @map_id_north.setter
    def map_id_north(self, value: Optional[str]):
        self._map_id_north = value

    @property
    def map_id_south(self) -> Optional[str]:
        """Map id where the Map is located"""
        return self._map_id_south

    @map_id_south.setter
    def map_id_south(self, value: Optional[str]):
        self._map_id_south = value

    @property
    def map_id_west(self) -> Optional[str]:
        """Map id where the Map is located"""
        return self._map_id_west

    @map_id_west.setter
    def map_id_west(self, value: Optional[str]):
        self._map_id_west = value

    @property
    def map_id_east(self) -> Optional[str]:
        """Map id where the Map is located"""
        return self._map_id_east

    @map_id_east.setter
    def map_id_east(self, value: Optional[str]):
        self._map_id_east = value


# TODO: Move in Room class
def is_closed_room(
    room_id: str, closed_rooms: dict[str, Commitment], now_hour: int, tm: TimeHandler
) -> bool:
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#is-closed-room"""
    cur_room_is_closed = False
    closed_rooms_to_del = []
    for id, item in closed_rooms.items():
        if id == room_id and tm.now_is_between(
            start=item.hour_start, end=item.hour_stop, now=now_hour
        ):
            cur_room_is_closed = True
        elif item.hour_stop != None and not tm.now_is_between(
            start=item.hour_start, end=item.hour_stop, now=now_hour
        ):
            closed_rooms_to_del.append(id)
    for id in closed_rooms_to_del:
        del closed_rooms[id]
    del closed_rooms_to_del
    return cur_room_is_closed


def get_room_by_id(room_id: str, rooms: list[Room]) -> Optional[Room]:
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-room"""
    if not room_id:
        log_warn("room_id is None", "nqtr.navigation.get_room_by_id()")
        return
    for room in rooms:
        if room.id == room_id:
            return room
    log_warn(f"Room with id {room_id} not found", "nqtr.navigation.get_room_by_id()")
    return


def get_location_by_id(
    location_id: str, locations: list[Location]
) -> Optional[Location]:
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-location"""
    if not location_id:
        log_error("location_id is None", "nqtr.navigation.get_location_by_id()")
        return
    for location in locations:
        if location.id == location_id:
            return location
    return
