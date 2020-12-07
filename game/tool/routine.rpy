init -9 python:
    class Commitment(object):
        """Commitment and routine"""
        def __init__(self,
            tm_start,
            tm_stop,
            chs = {},
            name=None,
            id_location=None,
            id_room=None,
            type=None,
            day_deadline=None):

            self.chs = chs
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.id_location = id_location
            self.id_room = id_room
            self.type = type
            self.day_deadline = day_deadline

        def getChIcons(self):
            icons = []
            for ch in self.chs.keys():
                icons.append(ch_icons.get(ch))
            return icons

        def talk(self, ch):
            ch_talk = ch
            Jump('talk')

    class TalkObject(object):
        def __init__(self,
            ch_secondary = [],
            image_non_talk=None,
            label_non_talk=None,
            image_talk=None,
            label_talk=None):

            self.ch_secondary = ch_secondary
            self.image_non_talk = image_non_talk
            self.label_non_talk = label_non_talk
            self.image_talk = image_talk
            self.label_talk = label_talk

    def clearExpiredSPRoutine():
        """removes expired Commitments"""
        rlist = []
        rlist.clear()
        for r in sp_routine:
            if (r.day_deadline != None and r.day_deadline <= tm.day):
                rlist.append(r)
        for r in rlist:
            sp_routine.remove(r)
        del rlist
        return

    def checkChLocation(id_location):
        """Returns the commitments of the NCPs in that Location at that time"""
        routines = {}
        for routine in df_routine.values():
            # Check Time and Location
            if (routine.id_location == id_location and tm.now_is_between(routine.tm_start, routine.tm_stop)):
                # Full verification
                chs = routine.chs
                for chKey in chs.keys():
                    routines[chKey] = routine
        return routines

    def whereIsLocation(ch):
        """returns the Location where a ch is located at that time"""
        # special routine
        for routine in sp_routine.values():
            if tm.now_is_between(routine.tm_start, routine.tm_stop):
                return routine.id_location
                if checkValidRoutineType(routine):
                    return routine.id_location
        # default routine
        location = None
        for routine in df_routine.values():
            if tm.now_is_between(routine.tm_start, routine.tm_stop):
                location = routine.id_location
                if checkValidRoutineType(routine):
                    return routine.id_location
        return location
