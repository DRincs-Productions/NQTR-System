# list of closed rooms is checked change_room
# is composed of id = room_id and Commitment()
# expired elements are checked in after_spending_time, if you don't want an expiration: tm_stop = None
default closed_rooms = {}

init -9 python:
    from typing import Optional

    class Room:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room """

        def __init__(self,
                    id: str,
                    location_id: str,
                    name: str = None,
                    icon: str = None,
                    bg: str = None,
                    action_ids: Optional[list[str]] = None):

            self.id = id
            self.location_id = location_id
            self.name = name
            self.icon = icon
            self.bg = bg
            self.action_ids = self.action_ids = action_ids if action_ids else []


    class Location:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location """
        # TODO: undiscovered locations

        def __init__(self,
                    id: str,
                    map_id: str,
                    external_room_id: str,
                    name: str = None,
                    icon: str = None,
                    xalign: int = 0,
                    yalign: int = 0):

            self.id = id
            self.map_id = map_id
            self.name = name
            self.external_room_id = external_room_id
            self.icon = icon
            self.xalign = xalign
            self.yalign = yalign


    def isClosedRoom(room_id: str, closed_rooms: dict[str, Commitment], tm: TimeHandler):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#is-closed-room """
        cur_room_is_closed = False
        closed_rooms_to_del = []
        for id, item in closed_rooms.items():
            if (id == room_id and tm.now_is_between(start=item.tm_start, end=item.tm_stop)):
                cur_room_is_closed = True
            elif (item.tm_stop != None and not tm.now_is_between(start=item.tm_start, end=item.tm_stop)):
                closed_rooms_to_del.append(id)
        for id in closed_rooms_to_del:
            del closed_rooms[id]
        del closed_rooms_to_del
        return cur_room_is_closed


    def changeRoom(room_id: str, rooms: list[Room], locations: list[Room]):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-room """
        new_room = None
        if not room_id:
            renpy.log("Warning: room_id is None")
            del new_room
            return
        for room in rooms:
            if room.id is str and room.id == room_id:
                new_room = room
        if new_room:
            prev_room = cur_room
            cur_room = new_room
        else:
            renpy.log("Error: cur_room is None")
            del new_room
            return
        del new_room
        changeLocation(cur_room.location_id, locations)
        return


    def changeLocation(location_id: str, locations: list[Room]):
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-location """
        if not location_id:
            renpy.log("Error: location_id is None")
            return
        for location in locations:
            if location.id is str and location.id == location_id:
                prev_location = cur_location
                cur_location = location
        return
