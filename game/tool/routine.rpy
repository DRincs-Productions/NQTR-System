init -9 python:
    class Commitment(object):
        """Commitment and routine"""
        def __init__(self, ch, tm_start, tm_stop, name='', id_location='', id_room='', type='', day_deadline='null'):
            self.ch = ch
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.id_location = id_location
            self.id_room = id_room
            self.type = type
            self.day_deadline = day_deadline

    def update_sp_routine():
        """removes expired Commitments"""
        rlist = []
        rlist.clear()
        for r in sp_routine:
            if (r.day_deadline != 'null' and r.day_deadline <= tm.day):
                rlist.append(r)
        for r in rlist:
            sp_routine.remove(r)

    def checkValidRoutineType(rt):
        """Check through a custom code if the rt is valid in vase to type"""
        # Custom code
        if (rt.type == "no_week"): #TODO: Checkweekend
            return True
        return False
