# list of closed rooms is checked change_room
# is composed of id = room_id and Commitment()
# expired elements are checked in after_wait, if you don't want an expiration: tm_stop = None
default closed_rooms = {}

init -9 python:
    from typing import Optional

    class Room:
        """Class of a Room"""

        def __init__(self,
                    id: str,
                    id_location: str,
                    name: str = None,
                    icon: str = None,
                    bg: str = None,
                    id_actions: Optional[list[str]] = None):

            self.id = id
            self.id_location = id_location
            self.name = name
            self.icon = icon
            self.bg = bg
            self.id_actions = self.id_actions = id_actions if id_actions else []


    class Location:
        """Class of a Location"""
        # TODO: undiscovered locations

        def __init__(self,
                    id: str,
                    id_map: str,
                    id_externalroom: str,
                    name: str = None,
                    icon: str = None,
                    xalign: int = 0,
                    yalign: int = 0):

            self.id = id
            self.id_map = id_map
            self.name = name
            self.id_externalroom = id_externalroom
            self.icon = icon
            self.xalign = xalign
            self.yalign = yalign


    def clearClosedRooms(closed_rooms: dict[str, Commitment]):
        "Deletes expired locked rooms. you want to add a room with no expiry date: tm_stop = None"
        closed_rooms_to_del = []
        for id, item in closed_rooms.items():
            if (item.tm_stop != None and tm.now_is_between(start=item.tm_start, end=item.tm_stop) == False):
                closed_rooms_to_del.append(id)
        for id in closed_rooms_to_del:
            del closed_rooms[id]
        del closed_rooms_to_del
        return closed_rooms
