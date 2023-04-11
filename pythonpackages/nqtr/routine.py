from typing import Optional

from pythonpackages.nqtr.action_talk import TalkObject
from pythonpackages.nqtr.time import MAX_DAY_HOUR, MIN_DAY_HOUR, TimeHandler


class Commitment(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#commitment
    event_label_name: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#events """

    def __init__(
        self,
        hour_start: int = MIN_DAY_HOUR,
        hour_stop: int = MAX_DAY_HOUR,
        ch_talkobj_dict: dict[str, Optional[TalkObject]] = {},
        background: Optional[str] = None,
        location_id: Optional[str] = None,
        room_id: Optional[str] = None,
        tag: Optional[str] = None,
        day_deadline: Optional[int] = None,
        event_label_name: Optional[str] = None
    ):

        self.background = background
        self.ch_talkobj_dict = ch_talkobj_dict
        self.hour_start = hour_start
        self.hour_stop = hour_stop-0.1
        self.location_id = location_id
        self.room_id = room_id
        self.tag = tag
        self.day_deadline = day_deadline
        self.event_label_name = event_label_name

    @property
    def hour_start(self) -> int:
        """The hour when the commitment starts."""
        return self._hour_start

    @hour_start.setter
    def hour_start(self, value: int):
        self._hour_start = value

    @property
    def hour_stop(self) -> int:
        """The hour when the commitment ends."""
        return self._hour_stop

    @hour_stop.setter
    def hour_stop(self, value: int):
        self._hour_stop = value

    @property
    def ch_talkobj_dict(self) -> dict[str, Optional[TalkObject]]:
        """Dictionary of characters and their TalkObject."""
        return self._ch_talkobj_dict

    @ch_talkobj_dict.setter
    def ch_talkobj_dict(self, value: dict[str, Optional[TalkObject]]):
        self._ch_talkobj_dict = value

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
    def tag(self) -> Optional[str]:
        """The tag of the commitment.
        # TODO: implement this"""
        return self._tag

    @tag.setter
    def tag(self, value: Optional[str]):
        self._tag = value

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
        return (self.event_label_name is not None)

    def getChIcons(self, ch_icons: dict[str, str]) -> list[str]:
        """returns a list of ch icons (not secondary ch)"""
        icons = []
        for ch in self.ch_talkobj_dict.keys():
            if (ch in ch_icons):
                icons.append(ch_icons[ch])
        return icons

    def getTalkBackground(self, ch: str) -> Optional[str]:
        "Returns the image during a conversation"
        if not self.ch_talkobj_dict[ch]:
            return None
        return self.ch_talkobj_dict[ch].conversation_background

    # doesn't seem to work
    # use something like this: renpy.call(cur_events_location[cur_room.id].event_label_name)
    # def start_event(self):
    #     if self.event_label_name == None:
    #         renpy.call(self.event_label_name)


def clearExpiredRoutine(commitments: dict[str, Commitment], tm: TimeHandler) -> None:
    """removes expired Commitments"""
    rlist = []
    rlist.clear()
    for key, val in commitments.items():
        if (val.day_deadline != None and val.day_deadline <= tm.day):
            rlist.append(key)
    for r in rlist:
        del commitments[r]
    del rlist
    return


def getChsInThisLocation(location_id: str, routine: dict[str, Commitment], tm: TimeHandler) -> dict[str, Commitment]:
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#priority """
    # Create a list of ch who have a commitment in that place at that time
    # It does not do enough checks, they will be done later with getChLocation()
    commitments = {}
    for comm in routine.values():
        # Check Time and Location
        if (comm.location_id == location_id and tm.now_is_between(start=comm.hour_start, end=comm.hour_stop)):
            # Full verification
            for chKey in comm.ch_talkobj_dict.keys():
                commitments[chKey] = None
    # Check I enter the current commitments of the ch.
    # In case the commitment is not in the place I want to go or they are null and void I delete the ch.
    commitments_key_to_del = []
    for ch in commitments.keys():
        commitments[ch] = getChLocation(ch, routine, tm)
        if commitments[ch] == None:
            commitments_key_to_del.append(ch)
        elif commitments[ch].location_id != location_id:
            commitments_key_to_del.append(ch)
    for ch in commitments_key_to_del:
        del commitments[ch]
    del commitments_key_to_del
    return commitments


def getEventsInThisLocation(location_id: str, routine: dict[str, Commitment], tm: TimeHandler) -> dict[str, Commitment]:
    """Returns events at that location at that time.
    Checks only in routine."""
    # Create a list of ch who have a commitment in that place at that time
    # It does not do enough checks, they will be done later with getChLocation()
    events = {}
    for comm in routine.values():
        # Check Time and Location and is event
        if (comm.location_id == location_id and tm.now_is_between(start=comm.hour_start, end=comm.hour_stop) and comm.is_event == True):
            events[comm.room_id] = comm
    return events


def getChLocation(ch: str, routine: dict[str, Commitment], tm: TimeHandler) -> Optional[Commitment]:
    """Returns the current commitment of the ch.
    Give priority to valid first found."""
    # special routine
    for id, comm in routine.items():
        if tm.now_is_between(start=comm.hour_start, end=comm.hour_stop):
            if ch in comm.ch_talkobj_dict:
                if (comm.tag != None):
                    if checkIfIsActiveByTag(tag=comm.tag, id=id):
                        return comm
                else:
                    return comm
    return None

# TODO To Move move in renpy


def checkIfIsActiveByTag(tag: str, id: str = "") -> bool:
    """Priority: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Tag#check-if-is-active-by-tag """
    # Custom code
    if (tag == None):
        return False
    if (tag == "no_week"):
        return True
    return False


def getBgRoomRoutine(commitments: dict[str, Commitment], room_id) -> Optional[str]:
    """Returns the first background image of the commitments based on the current room. if there are no returns None"""
    for item in commitments.values():
        if item.room_id == room_id:
            return item.background
    return
