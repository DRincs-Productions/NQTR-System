# if in a room there is a different bg (taken in routine) than usual, use this one
default sp_bg_change_room = None
# Image of a closed door
define bg_loc = "location/loc-[tm.image_time].webp"

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-room
label change_room(room_id = None, close=False):
    # start an event if it exists
    if room_id:
        $ changeRoom(room_id = room_id, rooms = rooms, locations = locations)
    call after_spending_time(close = close, is_check_event=True)
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#go-previous-room
label go_previous_room(close=False):
    $ cur_room = prev_room
    return

## Check if mc can come out
define block_goout_dialogue = _("Now is not the time to go outside")
label check_goout:
    if(not flags.get("goout")):
        "[block_goout_dialogue]"
        call screen room_navigation
    return

## Open the map or close the map
label open_map:
    call check_goout

    if not cur_location:
        call change_room(room_id = cur_room.location_id)
    scene expression map_images[cur_location.map_id] as bg

    if (not map_open):
        $ map_open = True
        call screen room_navigation
## Close the map
label close_map:
    python:
        for room in rooms:
            if(room.id == cur_location.external_room_id):
                cur_room = room
        map_open = False
    scene expression (cur_room.bg) as bg
    jump change_room

# Is opened in change_room when a room id is in closed rooms
label closed_room_event:
    # Custom code
    # if (cur_room == ...):
        # ...
    scene expression (bg_loc) as bg
    return
