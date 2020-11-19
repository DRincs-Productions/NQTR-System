init -9 python:
    class Commitment(object):
        """Commitment and routine"""
        def __init__(self,
            ch,
            tm_start,
            tm_stop,
            name=None,
            id_location=None,
            id_room=None,
            type=None,
            day_deadline=None):

            self.ch = ch
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.id_location = id_location
            self.id_room = id_room
            self.type = type
            self.day_deadline = day_deadline

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

    def checkValidRoutineType(rt):
        """Check through a custom code if the rt is valid in vase to type"""
        # Custom code
        if (rt.type == "no_week"): #TODO: Checkweekend
            return True
        return False

    def checkChLocation(id_location):
        """Returns the commitments of the NCPs in that Location at that time"""
        chs = []
        for ch_pos in df_routine.values():
            # Check Time and Location
            if (ch_pos.id_location == id_location and tm.now_is_between(ch_pos.tm_start, ch_pos.tm_stop)):
                # Full verification
                if (whereIsLocation(ch_pos.ch) == id_location):
                    chs.append(ch_pos)
        return chs

    def whereIsLocation(ch):
        """returns the Location where a ch is located at that time"""
        # special routine
        for ch_pos in sp_routine.values():
            if tm.now_is_between(ch_pos.tm_start, ch_pos.tm_stop):
                return ch_pos.id_location
                if checkValidRoutineType(ch_pos):
                    return ch_pos.id_location
        # default routine
        location = None
        for ch_pos in df_routine.values():
            if tm.now_is_between(ch_pos.tm_start, ch_pos.tm_stop):
                location = ch_pos.id_location
                if checkValidRoutineType(ch_pos):
                    return ch_pos.id_location
        return location
