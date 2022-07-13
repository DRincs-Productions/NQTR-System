# list of closed rooms is checked change_room
# is composed of id = room_id and Commitment()
# expired elements are checked in after_wait, if you don't want an expiration: tm_stop = None
default closed_rooms = {}

init -9 python:
    class Room:
        """Class of a Room"""

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
        """Class of a Location"""
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
        "Deletes expired locked rooms. you want to add a room with no expiry date: tm_stop = None"
        closed_rooms_to_del = []
        for id, item in closed_rooms.items():
            if (item.tm_stop != None and tm.now_is_between(start=item.tm_start, end=item.tm_stop) == False):
                closed_rooms_to_del.append(id)
        for id in closed_rooms_to_del:
            del closed_rooms[id]
        del closed_rooms_to_del
        return closed_rooms


    def changeRoom(room_id: str, rooms: list[Room], locations: list[Room]):
        for room in rooms:
            if room.id == room_id:
                cur_room = room
        for location in locations:
            if location.id == cur_room.location_id:
                cur_location = location
