define rooms = [
    ]

define locations = {
    }

define map_images = {
    }

define ch_icons = {
    }

default cur_room = rooms[0]
default cur_location = locations[cur_room.id_location]
# Variable to check the map screen: if it is True then the player is viewing the map.
default map_open = False
