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
        def __init__(self, ch, tm_start, tm_stop, name='', id_location='', id_room='', type=''):
            self.ch = ch
            self.tm_start = tm_start
            self.tm_stop = tm_stop-0.1
            self.id_location = id_location
            self.id_room = id_room
            self.type = type
