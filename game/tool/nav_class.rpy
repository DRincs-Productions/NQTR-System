# list of closed rooms is checked change_room
# is composed of id = room_id and Commitment()
# expired elements are checked in after_wait, if you don't want an expiration: tm_stop = None
default closed_rooms = {}

init -9 python:
    class Room:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room """

        def __init__(self,
                    id: str,
                    location_id: str,
                    name: str = None,
                    icon: str = None,
                    bg: str = None,
                    action_ids: list[str] = []):

            self.id = id
            self.location_id = location_id
            self.name = name
            self.icon = icon
            self.bg = bg
            self.action_ids = action_ids


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


    def clearClosedRooms(closed_rooms: dict[str, Commitment], tm: TimeHandler):
        """Deletes expired locked rooms. you want to add a room with no expiry date: tm_stop = None"""
        closed_rooms_to_del = []
        for id, item in closed_rooms.items():
            if (item.tm_stop != None and tm.now_is_between(start=item.tm_start, end=item.tm_stop) == False):
                closed_rooms_to_del.append(id)
        for id in closed_rooms_to_del:
            del closed_rooms[id]
        del closed_rooms_to_del
        return closed_rooms

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
                cur_location = location
        return
