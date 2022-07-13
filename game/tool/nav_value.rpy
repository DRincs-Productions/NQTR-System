define rooms = [
    Room(id="my_room", location_id="house", name=_("MC room"), icon="icon myroom", bg="bg myroom",action_ids = ["sleep","nap",]), 
    Room(id="alice_room", location_id="house", name=_("[a] room"), icon="icon aliceroom", bg="bg aliceroom"), 
    Room(id="bathroom", location_id="house", name=_("Bathroom"), icon="icon bathroom", bg="bg bathroom"), 
    Room(id="lounge", location_id="house", name=_("Lounge"), icon="icon lounge", bg="bg lounge"), 
    Room(id="terrace", location_id="house", name=_("Terrace"), icon="icon terrace", bg="bg terrace"), 
    Room(id="ann_room", location_id="house_Ann", name=_("Ann room"), icon="icon annroom", bg="bg annroom"),
    Room(id="courtyard", location_id="house_Ann", name=_("Courtyard"), icon="icon courtyard", bg="bg courtyard"), 
]

define locations = [
    Location(id = "house", map_id="map", external_room_id="terrace", name=_("MC house"), icon="icon map home", xalign=0.3, yalign=0.2),
]

define map_images = {
    "map"       :   "bg map",
}

define ch_icons = {
    "alice"     : "icon/Alice.webp",
    "ann"       : "icon/Ann.webp",
}

default cur_room = rooms[0]
default cur_location = locations[0]
# Variable to check the map screen: if it is True then the player is viewing the map.
default map_open = False
