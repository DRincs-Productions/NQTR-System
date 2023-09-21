from typing import Optional, Union

from pythonpackages.nqtr.action_talk import TalkObject
from pythonpackages.nqtr.disabled_solution import DisabledClass
from pythonpackages.nqtr.time import MAX_DAY_HOUR, MIN_DAY_HOUR, TimeHandler
from pythonpackages.renpy_utility.character_custom import DRCharacter
from pythonpackages.renpy_utility.renpy_custom_log import log_info


class Commitment(DisabledClass):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#commitment
    event_label_name: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#events
    """

    def __init__(
        self,
        hour_start: Union[int, float] = MIN_DAY_HOUR,
        hour_stop: Union[int, float] = MAX_DAY_HOUR,
        characters: Optional[Union[list[str], str]] = [],
        ch_talkobj_dict: dict[str, Optional[TalkObject]] = {},
        background: Optional[str] = None,
        location_id: Optional[str] = None,
        room_id: Optional[str] = None,
        day_deadline: Optional[int] = None,
        event_label_name: Optional[str] = None,
        disabled: Union[bool, str] = False,
    ):
        # Button init
        super().__init__(disabled=disabled)
        # Fix a character values
        if characters:
            if isinstance(characters, str):
                characters = [characters]
            for ch in characters:
                if ch not in ch_talkobj_dict:
                    ch_talkobj_dict[ch] = None
        # Commitment init
        self.background = background
        self.ch_talkobj_dict = ch_talkobj_dict
        self.hour_start = hour_start
        self.hour_stop = hour_stop - 0.1
        self.location_id = location_id
        self.room_id = room_id
        self.day_deadline = day_deadline
        self.event_label_name = event_label_name

    @property
    def hour_start(self) -> Union[int, float]:
        """The hour when the commitment starts."""
        return self._hour_start

    @hour_start.setter
    def hour_start(self, value: Union[int, float]):
        self._hour_start = value

    @property
    def hour_stop(self) -> Union[int, float]:
        """The hour when the commitment ends."""
        return self._hour_stop

    @hour_stop.setter
    def hour_stop(self, value: Union[int, float]):
        self._hour_stop = value

    @property
    def ch_talkobj_dict(self) -> dict[str, Optional[TalkObject]]:
        """Dictionary of characters and their TalkObject."""
        return self._ch_talkobj_dict

    @ch_talkobj_dict.setter
    def ch_talkobj_dict(self, value: dict[str, Optional[TalkObject]]):
        self._ch_talkobj_dict = value

    @property
    def characters(self) -> list[str]:
        """List of characters"""
        return list(self.ch_talkobj_dict.keys())

    @property
    def background(self) -> Optional[str]:
        "Image path shown when standing at the Commitment site. And it is also the image shown before and after the conversation with a character"
        return self._bg

    @background.setter
    def background(self, value: Optional[str]):
        self._bg = value

    @property
    def location_id(self) -> Optional[str]:
        """The location where the commitment takes place."""
        return self._location_id

    @location_id.setter
    def location_id(self, value: Optional[str]):
        self._location_id = value

    @property
    def room_id(self) -> Optional[str]:
        """The room where the commitment takes place."""
        return self._room_id

    @room_id.setter
    def room_id(self, value: Optional[str]):
        self._room_id = value

    @property
    def day_deadline(self) -> Optional[int]:
        """The day when the commitment expires."""
        return self._day_deadline

    @day_deadline.setter
    def day_deadline(self, value: Optional[int]):
        self._day_deadline = value

    @property
    def event_label_name(self) -> Optional[str]:
        """The event label name."""
        return self._event_label_name

    @event_label_name.setter
    def event_label_name(self, value: Optional[str]):
        self._event_label_name = value

    @property
    def is_event(self) -> bool:
        "Returns True if it is an event: if you go to the room of the having the event label it will start an automatic."
        return self.event_label_name is not None

    def character_icons(self, character_dict: dict[str, DRCharacter]) -> list[str]:
        """Returns a list of paths to the icons of the characters in the commitment."""
        icons: list[str] = []
        for ch in self.characters:
            if ch in character_dict:
                icons.append(character_dict[ch].icon)
        return icons

    def conversation_background(self, ch: str) -> Optional[str]:
        "Returns the image during a conversation"
        item = self.ch_talkobj_dict[ch]
        if isinstance(item, TalkObject):
            return item.conversation_background
        else:
            return None

    # doesn't seem to work
    # use something like this: renpy.call(cur_events_location[cur_room.id].event_label_name)
    # def start_event(self):
    #     if self.event_label_name == None:
    #         renpy.call(self.event_label_name)


def clear_expired_routine(commitments: dict[str, Commitment], tm: TimeHandler) -> None:
    """removes expired Commitments"""
    rlist = []
    rlist.clear()
    for key, val in commitments.items():
        if val.day_deadline != None and val.day_deadline <= tm.day:
            rlist.append(key)
    for r in rlist:
        del commitments[r]
    del rlist
    return


def characters_commitment_in_current_location(
    location_id: str,
    routine: dict[str, Commitment],
    tm: TimeHandler,
    flags: dict[str, bool] = {},
) -> dict[str, Commitment]:
    """Priority wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#priority"""
    # Create a list of ch who have a commitment in that place at that time
    # It does not do enough checks, they will be done later with commitment_by_character()
    characters_into_current_location: list[str] = []
    for comm in routine.values():
        # Check Time and Location
        if (
            comm.location_id == location_id
            and tm.now_is_between(start=comm.hour_start, end=comm.hour_stop)
            and not comm.is_disabled(flags)
        ):
            for chKey in comm.characters:
                if chKey not in characters_into_current_location:
                    characters_into_current_location.append(chKey)
    # Check I enter the current commitments of the ch.
    # In case the commitment is not in the place I want to go or they are null and void I delete the ch.
    commitments: dict[str, Commitment] = {}
    for ch in characters_into_current_location:
        commitment_item = commitment_by_character(ch, routine, tm, flags)
        # the item can be None if the commitment is disabled
        # the item can be in another location, because the character has a commitment in another location whit more priority
        if commitment_item is not None and commitment_item.location_id == location_id:
            commitments[ch] = commitment_item
    del characters_into_current_location
    return commitments


def characters_events_in_current_location(
    location_id: str,
    routine: dict[str, Commitment],
    tm: TimeHandler,
    flags: dict[str, bool] = {},
) -> dict[str, Commitment]:
    """Returns events at that location at that time.
    Checks only in routine."""
    # Create a list of ch who have a commitment in that place at that time
    # It does not do enough checks, they will be done later with commitment_by_character()
    events = {}
    for comm in routine.values():
        # Check Time and Location and is event
        if (
            comm.location_id == location_id
            and tm.now_is_between(start=comm.hour_start, end=comm.hour_stop)
            and comm.is_event == True
            and not comm.is_disabled(flags)
        ):
            events[comm.room_id] = comm
    return events


def commitment_by_character(
    ch: str,
    routine: dict[str, Commitment],
    tm: TimeHandler,
    flags: dict[str, bool] = {},
) -> Optional[Commitment]:
    """Returns the current commitment of the ch.
    Give priority to valid first found."""
    # special routine
    for id, comm in routine.items():
        if tm.now_is_between(start=comm.hour_start, end=comm.hour_stop):
            if ch in comm.ch_talkobj_dict:
                if not comm.is_disabled(flags):
                    return comm
    return None


def commitment_background(
    commitments: dict[str, Commitment], room_id: str
) -> Optional[str]:
    """Returns the first background image of the commitments based on the current room. if there are no returns None"""
    for item in commitments.values():
        if item and item.room_id == room_id:
            return item.background
    return
