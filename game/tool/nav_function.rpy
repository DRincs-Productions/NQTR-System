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
        location = ''
        for ch_pos in df_routine:
            if tm.now_is_between(ch_pos.tm_start, ch_pos.tm_stop):
                location = ch_pos.id_location
                # Custom code
                if (ch_pos.type == "no_week"): #TODO: Checkweekend
                    return ch_pos.id_location
        return location

    def enterRoom(id):
        """Manages the possibility of entering a room or not"""
        # Custom code
        return True
