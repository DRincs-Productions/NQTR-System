init -10 python:
    class Commitment(object):
        """Commitment, routine and event"""

        def __init__(self,
                    tm_start: int,
                    tm_stop: int,
                    ch_talkobj_dict: dict[str, TalkObject] = {},
                    bg: str  = None,
                    name: str = None,
                    location_id: str = None,
                    room_id: str = None,
                    type: str = None,
                    day_deadline: int = None,
                    event_label_name: str = None
                    ):

            # TODO: add a function that checks if it is available to talk (maybe with flags)
            # TODO: add the case in which after an avent the ch is no longer available to speak for a certain period of time
            # TODO: add event: in case it is nothing then when MC enter in that room starts a label
            self.bg = bg
            self.ch_talkobj_dict = ch_talkobj_dict
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.location_id = location_id
            self.room_id = room_id
            self.type = type
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

        def getChIcons(self, ch_icons: dict[str, str]):
            """returns a list of ch icons (not secondary ch)"""
            icons = []
            for ch in self.ch_talkobj_dict.keys():
                if (ch in ch_icons):
                    icons.append(ch_icons[ch])
            return icons

        def getTalkBackground(self, ch):
            "Returns the image during a conversation"
            return self.ch_talkobj_dict[ch].getBackground()

        def getBackground(self):
            "Returns the BeforeTalk image of the first ch that has it. Otherwise None"
            return self.bg

        def getBackgroundAfter(self):
            "Returns the AfterTalk image of the ch or the first that has it. Otherwise None"
            return self.bg

        def isEvent(self):
            "Returns True if it is an event: if you go to the room of the having the event label it will start an automatic."
            return (self.event_label_name is not None)

        # doesn't seem to work
        # use something like this: renpy.call(cur_events_location[cur_room.id].event_label_name)
        # def start_event(self):
        #     if self.event_label_name == None:
        #         renpy.call(self.event_label_name)


    def clearExpiredRoutine(routine: dict[str, Commitment], tm: TimeHandler):
        """removes expired Commitments"""
        rlist = []
        rlist.clear()
        for key, val in routine.iteritems():
            if (val.day_deadline != None and val.day_deadline <= tm.day):
                rlist.append(key)
        for r in rlist:
            del routine[r]
        del rlist
        return routine


    def getChsInThisLocation(location_id: str):
        # TODO: to add when I change location_id
        """Returns the commitments of the ch (NCPs) in that Location at that time.
        Give priority to special routine, and routine with a valid type."""
        # Create a list of ch who have a routine in that place at that time
        # It does not do enough checks, they will be done later with getChLocation()
        routines = {}
        for routine in sp_routine.values():
            # Check Time and Location
            if (routine.location_id == location_id and tm.now_is_between(start=routine.tm_start, end=routine.tm_stop)):
                # Full verification
                for chKey in routine.ch_talkobj_dict.keys():
                    routines[chKey] = None
        for routine in df_routine.values():
            # Check Time and Location
            if (routine.location_id == location_id and tm.now_is_between(start=routine.tm_start, end=routine.tm_stop)):
                # Full verification
                ch_talkobj_dict = routine.ch_talkobj_dict
                for chKey in ch_talkobj_dict.keys():
                    routines[chKey] = None
        # Check I enter the current routines of the ch.
        # In case the routine is not in the place I want to go or they are null and void I delete the ch.
        routines_key_to_del = []
        for ch in routines.keys():
            routines[ch] = getChLocation(ch)
            if routines[ch] == None:
                routines_key_to_del.append(ch)
            elif routines[ch].location_id != location_id:
                routines_key_to_del.append(ch)
        for ch in routines_key_to_del:
            del routines[ch]
        del routines_key_to_del
        return routines


    def getEventsInThisLocation(location_id: str, sp_routine: dict[str, Commitment]):
        # TODO: to add when I change location_id
        """Returns events at that location at that time.
        Checks only in sp_routine."""
        # Create a list of ch who have a routine in that place at that time
        # It does not do enough checks, they will be done later with getChLocation()
        events = {}
        for routine in sp_routine.values():
            # Check Time and Location and is event
            if (routine.location_id == location_id and tm.now_is_between(start=routine.tm_start, end=routine.tm_stop) and routine.isEvent() == True):
                events[routine.room_id] = routine
        return events


    def getChLocation(ch: str):
        """Returns the current routine of the ch.
        Give priority to special routine, and routine with a valid type."""
        ret_routine = None
        # special routine
        for routine in sp_routine.values():
            if tm.now_is_between(start=routine.tm_start, end=routine.tm_stop):
                if ch in routine.ch_talkobj_dict:
                    ret_routine = routine
                    if checkValidType(routine):
                        return routine
        if ret_routine != None:
            return ret_routine
        # default routine
        for routine in df_routine.values():
            if tm.now_is_between(start=routine.tm_start, end=routine.tm_stop):
                if ch in routine.ch_talkobj_dict:
                    ret_routine = routine
                    if checkValidType(routine.type):
                        return routine
        return ret_routine


    # TODO: Is not used in Routine so move, maybe it is better in boolean_value
    def checkValidType(type):
        """Check according to its type, if it is True or False"""
        # Custom code
        if (type == None):
            return False
        if (type == "no_week"):
            # TODO: Checkweekend
            return True
        return False


    def getBgRoomRoutine(routines, room_id):
        """Returns the first background image of the routines based on the current room. if there are no returns None"""
        for item in routines.values():
            if item.room_id == room_id:
                return item.getBackground()
        return None
