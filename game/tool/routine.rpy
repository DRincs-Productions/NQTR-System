# special routine of the NCP
# they are added after completing missions or for some other reason.
# if there is another commitment in the default routine at the same time, it will be "overwritten"
default sp_routine = []

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

