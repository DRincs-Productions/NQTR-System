# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room
define rooms = [
    Room(id="my_room", location_id="house", name=_("MC room"), button_icon="icon myroom", bg="bg myroom",action_ids = ["sleep","nap",]), 
    Room(id="alice_room", location_id="house", name=_("[a] room"), button_icon="icon aliceroom", bg="bg aliceroom"), 
    Room(id="bathroom", location_id="house", name=_("Bathroom"), button_icon="icon bathroom", bg="bg bathroom"), 
    Room(id="lounge", location_id="house", name=_("Lounge"), button_icon="icon lounge", bg="bg lounge"), 
    Room(id="terrace", location_id="house", name=_("Terrace"), button_icon="icon terrace", bg="bg terrace"), 
    Room(id="ann_room", location_id="house_Ann", name=_("Ann room"), button_icon="icon annroom", bg="bg annroom"),
    Room(id="courtyard", location_id="house_Ann", name=_("Courtyard"), button_icon="icon courtyard", bg="bg courtyard"), 
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location
define locations = [
    Location(id = "house", map_id="map", external_room_id="terrace", name=_("MC house"), picture_in_background="icon map home", xpos=0.3, ypos=0.2),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map
define map_images = {
    "map"       :   "bg map",
}

# TODO: Wiki
define ch_icons = {
    "alice"     : "icon/Alice.webp",
    "ann"       : "icon/Ann.webp",
}

default prev_room = None
default cur_room = rooms[0]
default cur_location = locations[0]
# Variable to check the map screen: if it is True then the player is viewing the map.
default map_open = False
