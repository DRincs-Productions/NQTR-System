# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room
define rooms = [
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location
define locations = [
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map
define maps = {
}

# TODO: Wiki
define ch_icons = {
}

default prev_room = None
default cur_room = rooms[0]
default prev_location = None
default cur_location = locations[0]
default cur_map_id = cur_location.map_id
# Variable to check the map screen: if it is True then the player is viewing the map.
default map_open = False
