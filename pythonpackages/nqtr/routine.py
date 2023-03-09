from typing import Optional
from pythonpackages.nqtr.action_talk import TalkObject
from pythonpackages.nqtr.time import TimeHandler


class Commitment(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#commitment
    event_label_name: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Routine-system#events """

    def __init__(self,
                tm_start: int,
                tm_stop: int,
                ch_talkobj_dict: dict[str, TalkObject] = {},
                bg: str = None,
                name: str = None,
                location_id: str = None,
                room_id: str = None,
                tag: str = None,
                day_deadline: int = None,
                event_label_name: str = None
                ):

        self.bg = bg
        self.ch_talkobj_dict = ch_talkobj_dict
        self.tm_start = tm_start
        self.tm_stop = tm_stop-0.1
        self.location_id = location_id
        self.room_id = room_id
        self.tag = tag
        self.day_deadline = day_deadline
        # ATTENTION: in check_event_sp if the mc has not moved, delete the event (resolves any loops)
        # se si vuole degli eventi fissi usare check_event_df
        # if you want the event to be started only once and then deleted
        # at the end of the label insert:
        # return
        # if you want the event to be repeated every time you go to that room
        # at the end of the label insert:
        # call change_room
        # if you want the event to be repeated only once, but then it is repeated after waiting some time or changing location_id
        # at the end of the label insert:
        # $ del cur_events_location[cur_room.id]    # cur_room.id: i.e. the id of the room where the event is triggered
        # call change_room
        self.event_label_name = event_label_name

    def getChIcons(self, ch_icons: dict[str, str]) -> list[str]:
        """returns a list of ch icons (not secondary ch)"""
        icons = []
        for ch in self.ch_talkobj_dict.keys():
            if (ch in ch_icons):
                icons.append(ch_icons[ch])
        return icons

    def getTalkBackground(self, ch: str) -> str:
        "Returns the image during a conversation"
        return self.ch_talkobj_dict[ch].getBackground()

    def getBackground(self) -> str:
        "Returns the BeforeTalk image of the first ch that has it. Otherwise None"
        return self.bg

    def isEvent(self) -> bool:
        "Returns True if it is an event: if you go to the room of the having the event label it will start an automatic."
        return (self.event_label_name is not None)

    # doesn't seem to work
    # use something like this: renpy.call(cur_events_location[cur_room.id].event_label_name)
    # def start_event(self):
    #     if self.event_label_name == None:
    #         renpy.call(self.event_label_name)


def clearExpiredRoutine(commitments: dict[str, Commitment], tm: TimeHandler) -> None:
    """removes expired Commitments"""
    rlist = []
    rlist.clear()
    for key, val in commitments.iteritems():
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
        if (comm.location_id == location_id and tm.now_is_between(start=comm.tm_start, end=comm.tm_stop)):
            # Full verification
            for chKey in comm.ch_talkobj_dict.keys():
                commitments[chKey] = None
    # Check I enter the current commitments of the ch.
    # In case the commitment is not in the place I want to go or they are null and void I delete the ch.
    commitments_key_to_del = []
    for ch in commitments.keys():
        commitments[ch] = getChLocation(ch, routine)
        if commitments[ch] == None:
            commitments_key_to_del.append(ch)
        elif commitments[ch].location_id != location_id:
            commitments_key_to_del.append(ch)
    for ch in commitments_key_to_del:
        del commitments[ch]
    del commitments_key_to_del
    return commitments


def getEventsInThisLocation(location_id: str, routine: dict[str, Commitment]) -> dict[str, Commitment]:
    """Returns events at that location at that time.
    Checks only in routine."""
    # Create a list of ch who have a commitment in that place at that time
    # It does not do enough checks, they will be done later with getChLocation()
    events = {}
    for comm in routine.values():
        # Check Time and Location and is event
        if (comm.location_id == location_id and tm.now_is_between(start=comm.tm_start, end=comm.tm_stop) and comm.isEvent() == True):
            events[comm.room_id] = comm
    return events


def getChLocation(ch: str, routine: dict[str, Commitment]) -> Optional[Commitment]:
    """Returns the current commitment of the ch.
    Give priority to ActiveByTag after first_found."""
    first_found_commitment = None
    # special routine
    for id, comm in routine.items():
        if tm.now_is_between(start=comm.tm_start, end=comm.tm_stop):
            if ch in comm.ch_talkobj_dict:
                if (first_found_commitment == None)
                    first_found_commitment = comm
                if checkIfIsActiveByTag(tag=comm.tag, id=id):
                    return comm
    return first_found_commitment


def checkIfIsActiveByTag(tag: str, id: str = None) -> bool:
    """Priority: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Tag#check-if-is-active-by-tag """
    # Custom code
    if (tag == None):
        return False
    if (tag == "no_week"):
        return True
    return False


def getBgRoomRoutine(commitments: dict[str, Commitment], room_id) -> None:
    """Returns the first background image of the commitments based on the current room. if there are no returns None"""
    for item in commitments.values():
        if item.room_id == room_id:
            return item.getBackground()
    return
