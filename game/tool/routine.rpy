init -9 python:
    class Commitment(object):
        """Commitment, routine and event"""
        def __init__(self,
            tm_start,
            tm_stop,
            chs = {},
            name=None,
            id_location=None,
            id_room=None,
            type=None,
            day_deadline=None,
            label_event=None):

            # TODO: add a function that checks if it is available to talk (maybe with bl_values)
            # TODO: add the case in which after an avent the ch is no longer available to speak for a certain period of time
            # TODO: add event: in case it is nothing then when MC enter in that room starts a label
            self.chs = chs
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.id_location = id_location
            self.id_room = id_room
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
            # if you want the event to be repeated only once, but then it is repeated after waiting some time or changing id_location
            # at the end of the label insert:
                # $ cur_events_location.pop(cur_room.id)    # cur_room.id: i.e. the id of the room where the event is triggered
                # call change_room
            self.label_event = label_event

        def getChIcons(self):
            """returns a list of ch icons (not secondary ch)"""
            icons = []
            for ch in self.chs.keys():
                icons.append(ch_icons[ch])
            return icons

        def talk(self, ch):
            """Start talk() of TalkObject() of ch."""

            # TODO: it doesn't matter i don't know why
            talk_ch = ch
            # TODO: use this:
            # action [Hide('wait_navigation'), SetVariable('talk_ch', ch), SetVariable('talk_image', routine.getTalkImage(ch)), SetVariable('talk_end_image', routine.getAfterTalkImage(ch)), Function(routine.talk, ch)]

            if self.chs[ch].talk() == False:
                for ch in self.chs.values():
                    if ch.insertBgImage():
                        return

            # TODO: otherwise insert the bg of the current room

        def getTalkImage(self, ch):
            "Returns the image during a conversation"
            return self.chs[ch].getTalkImage()

        def getBeforeTalkImage(self):
            "Returns the BeforeTalk image of the first ch that has it. Otherwise None"
            for ch in self.chs.values():
                if ch.getAfterTalkImage() != None:
                    return ch.getAfterTalkImage()
            return None

        def getAfterTalkImage(self, ch):
            "Returns the AfterTalk image of the ch or the first that has it. Otherwise None"
            if self.chs[ch].getAfterTalkImage() != None:
                return self.chs[ch].getAfterTalkImage()
            else:
                return self.getBeforeTalkImage()

        def is_event(self):
            "Returns True if it is an event: if you go to the room of the having the event label it will start an automatic."
            return (self.label_event is not None)

        # doesn't seem to work
        # use something like this: renpy.call(cur_events_location[cur_room.id].label_event)
        # def start_event(self):
        #     if self.label_event == None:
        #         renpy.call(self.label_event)

    class TalkObject(object):
        """At the inside of the class there are the values used for the talk() function, 
        (all this could be done in Commitment(), but I preferred not to use a dictionary)"""
        def __init__(self,
            ch_secondary = [],
            bg_before_after=None,
            after_label_event=None,
            bg_talk=None,
            label_talk=None):

            self.ch_secondary = ch_secondary
            self.bg_before_after = bg_before_after
            self.bg_talk = bg_talk
            self.after_label_event = after_label_event
            self.label_talk = label_talk

        def talk(self):
            """Inside you can find the labels and images to start talk()"""
            # if label_talk == None does the default procedure
            if self.label_talk == None:
                renpy.jump('talk')
            else:
                renpy.jump(self.label_talk)

        def getTalkImage(self):
            """Returns the image during a conversation"""
            return self.bg_talk

        def getBeforeTalkImage(self):
            """Returns the background image used when someone is in the same room. It can be None"""
            return self.bg_before_after

        def getAfterTalkImage(self):
            """Returns the background image used after a conversation, 
            but if after_label_event is not null it passes to after_label_event. 
            ((the latter can be used in case the room is no longer accessible and thus takes you to another room))"""
            if self.after_label_event != None:
                renpy.jump(after_label_event)
            else:
                return self.bg_before_after

    def clearExpiredSPRoutine():
        """removes expired Commitments"""
        rlist = []
        rlist.clear()
        for key, val in sp_routine.iteritems():
            if (val.day_deadline != None and val.day_deadline <= tm.day):
                rlist.append(key)
        for r in rlist:
            del sp_routine[r]
        del rlist
        return

    def getChsInThisLocation(id_location):
        # TODO: to add when I change id_location
        """Returns the commitments of the ch (NCPs) in that Location at that time.
        Give priority to special routine, and routine with a valid type."""
        # Create a list of ch who have a routine in that place at that time
        # It does not do enough checks, they will be done later with getChLocation()
        routines = {}
        for routine in sp_routine.values():
            # Check Time and Location
            if (routine.id_location == id_location and tm.now_is_between(start=routine.tm_start, end=routine.tm_stop)):
                # Full verification
                for chKey in routine.chs.keys():
                    routines[chKey] = None
        for routine in df_routine.values():
            # Check Time and Location
            if (routine.id_location == id_location and tm.now_is_between(start=routine.tm_start, end=routine.tm_stop)):
                # Full verification
                chs = routine.chs
                for chKey in chs.keys():
                    routines[chKey] = None
        # Check I enter the current routines of the ch.
        # In case the routine is not in the place I want to go or they are null and void I delete the ch.
        for ch in routines.keys():
            routines[ch] = getChLocation(ch)
            if routines[ch] == None:
                del routines[ch]
            elif routines[ch].id_location != id_location:
                del routines[ch]
        return routines

    def getEventsInThisLocation(id_location):
        # TODO: to add when I change id_location
        """Returns events at that location at that time.
        Checks only in sp_routine."""
        # Create a list of ch who have a routine in that place at that time
        # It does not do enough checks, they will be done later with getChLocation()
        events = {}
        for routine in sp_routine.values():
            # Check Time and Location and is event
            if (routine.id_location == id_location and tm.now_is_between(start=routine.tm_start, end=routine.tm_stop) and routine.is_event() == True):
                events[routine.id_room] = routine
        return events

    def getChLocation(ch):
        """Returns the current routine of the ch.
        Give priority to special routine, and routine with a valid type."""
        ret_routine = None
        # special routine
        for routine in sp_routine.values():
            if tm.now_is_between(start=routine.tm_start, end=routine.tm_stop):
                if ch in routine.chs:
                    ret_routine = routine
                    if checkValidType(routine):
                        return routine
        if ret_routine != None:
            return ret_routine
        # default routine
        for routine in df_routine.values():
            if tm.now_is_between(start=routine.tm_start, end=routine.tm_stop):
                if ch in routine.chs:
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
            if item.id_room == room_id:
                return item.getBeforeTalkImage()
        return None
