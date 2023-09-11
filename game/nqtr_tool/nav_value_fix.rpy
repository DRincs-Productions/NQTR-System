init python:
    from pythonpackages.nqtr.navigation import Room
    from pythonpackages.nqtr.navigation import Location
    from pythonpackages.nqtr.navigation import Map

    if not "rooms" in locals() | globals():
        rooms = []
        rooms.append(Room(id="empty", name="empty", location_id="empty"))
    if not "locations" in locals() | globals():
        locations = []
        locations.append(Location(id = "empty", name="empty", map_id="empty", external_room_id="empty"))
    if not "maps" in locals() | globals():
        maps = {
            "empty": Map(
                name="empty",
                background = "",
            )
        }
