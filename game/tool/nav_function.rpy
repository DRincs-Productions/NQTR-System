init python:
    def checkChLocation(id_location):
        """Returns the commitments of the NCPs in that Location at that time"""
        chs = []
        for ch_pos in df_routine:
            # Check Time and Location
            if (ch_pos.id_location == id_location and tm.now_is_between(ch_pos.tm_start, ch_pos.tm_stop)):
                # Full verification
                if (whereIsLocation(ch_pos.ch) == id_location):
                    chs.append(ch_pos)
        return chs

    def whereIsLocation(ch):
        """returns the Location where a ch is located at that time"""
        # special routine
        for ch_pos in sp_routine:
            if tm.now_is_between(ch_pos.tm_start, ch_pos.tm_stop):
                return ch_pos.id_location
                if checkValidRoutineType(ch_pos):
                    return ch_pos.id_location
        # default routine
        location = ''
        for ch_pos in df_routine:
            if tm.now_is_between(ch_pos.tm_start, ch_pos.tm_stop):
                location = ch_pos.id_location
                if checkValidRoutineType(ch_pos):
                    return ch_pos.id_location
        return location

    def enterRoom(id):
        """Manages the possibility of entering a room or not"""
        # Custom code
        return True
