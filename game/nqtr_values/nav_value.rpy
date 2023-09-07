init python:
    from pythonpackages.nqtr.navigation import Room
    from pythonpackages.nqtr.navigation import Location
    from pythonpackages.nqtr.navigation import Map

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#room
define rooms = [
    Room(id="my_room", location_id="house", name=_("MC room"), button_icon="icon myroom", background ="bg myroom",action_ids = ["sleep","nap",]), 
    Room(id="alice_room", location_id="house", name=_("[a] room"), button_icon="icon aliceroom", background ="bg aliceroom"), 
    Room(id="bathroom", location_id="house", name=_("Bathroom"), button_icon="icon bathroom", background ="bg bathroom"), 
    Room(id="lounge", location_id="house", name=_("Lounge"), button_icon="icon lounge", background ="bg lounge"), 
    Room(id="terrace", location_id="house", name=_("Terrace"), button_icon="icon terrace", background ="bg terrace"), 
    Room(id="ann_room", location_id="house_Ann", name=_("Ann room"), button_icon="icon annroom", background ="bg annroom"),
    Room(id="courtyard", location_id="house_Ann", name=_("Courtyard"), button_icon="icon courtyard", background ="bg courtyard"), 
    Room(id="gym_room", location_id="gym", name=_("Gym"), button_icon="icon gym", background ="bg gym"), 
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#location
define locations = [
    Location(id = "house", map_id="map", external_room_id="terrace", name=_("MC house"), picture_in_background="icon map home", xalign=0.3, yalign=0.2),
    Location(id = "gym", map_id="map", external_room_id="gym_room", name=_("Gym"), picture_in_background="icon map gym", xalign=0.5, yalign=0.3),
]

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#map
define maps = {
    "map": Map(
        name = _("Map"), background = "bg map",
        map_id_north = "nightcity",
        map_id_south = None,
        map_id_west = None,
        map_id_east = None,
    ),
    "nightcity": Map(
        name = _("Night City"), background = "bg nightcity",
        map_id_north = None,
        map_id_south = "map",
        map_id_west = None,
        map_id_east = None,
    ),
}
