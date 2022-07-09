define rooms = [
        Room(id="my_room", id_location="house", name=_("MC room"), icon="icon myroom", bg="bg myroom",id_actions = ["sleep","nap",]), 
        Room(id="alice_room", id_location="house", name=_("[a] room"), icon="icon aliceroom", bg="bg aliceroom"), 
        Room(id="bathroom", id_location="house", name=_("Bathroom"), icon="icon bathroom", bg="bg bathroom"), 
        Room(id="lounge", id_location="house", name=_("Lounge"), icon="icon lounge", bg="bg lounge"), 
        Room(id="terrace", id_location="house", name=_("Terrace"), icon="icon terrace", bg="bg terrace"), 
        Room(id="ann_room", id_location="house_Ann", name=_("Ann room"), icon="icon annroom", bg="bg annroom"),
        Room(id="courtyard", id_location="house_Ann", name=_("Courtyard"), icon="icon courtyard", bg="bg courtyard"), 
]

define locations = {
        "house"     :   Location(id = "house", key_map="map", id_externalroom="terrace", name=_("MC house"), icon="icon map home", xalign=0.3, yalign=0.2), 
}

define map_images = {
        "map"       :   "bg map",
}

define ch_icons = {
        "alice"     : "icon/Alice.webp",
        "ann"       : "icon/Ann.webp",
}

default cur_room = rooms[0]
default cur_location = locations[cur_room.id_location]
# Variable to check the map screen: if it is True then the player is viewing the map.
default map_open = False
