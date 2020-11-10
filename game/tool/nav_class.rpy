init -9 python:
    class Room:
        """Class of a Room"""
        def __init__(self, id, id_location, name='', icon=''):
            self.id = id
            self.id_location = id_location
            self.name = name
            self.icon = icon
        def enter(self):
            return enterRoom(id = self.id)

    class Commitment(object):
        """Commitment"""
        def __init__(self, ch, tp_start, tp_stop, name='', id_location='', id_room='', type=''):
            self.ch = ch
            self.tp_start = tp_start
            self.tp_stop = tp_stop
            self.id_location = id_location
            self.id_room = id_room
            self.type = type
