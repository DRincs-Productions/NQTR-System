init -9 python:
    class Room:
        """Class of a Room"""
        def __init__(self,
            id,
            id_location,
            name=None,
            icon=None,
            bg=None,
           id_actions=[]):

            self.id = id
            self.id_location = id_location
            self.name = name
            self.icon = icon
            self.bg = bg
            self.id_actions = id_actions

    class Location:
        """Class of a Location"""
        # TODO: undiscovered locations
        def __init__(self,
            id,
            key_map,
            id_externalroom,
            name=None,
            icon=None,
            xalign=0,
            yalign=0):

            self.id = id
            self.key_map = key_map
            self.name = name
            self.id_externalroom = id_externalroom
            self.icon = icon
            self.xalign = xalign
            self.yalign = yalign

# list of closed rooms is checked change_room
# is composed of id = room_id and Commitment()
# expired elements are checked in after_wait, if you don't want an expiration: tm_stop = None
default closed_rooms = {}
init -9 python:
    def clearClosedRooms():
        "Deletes expired locked rooms. you want to add a room with no expiry date: tm_stop = None"
        for id, item in closed_rooms.items():
            if (item.tm_stop != None and tm.now_is_between(start=item.tm_start, end=item.tm_stop) == False):
                closed_rooms.pop(id)
        return
