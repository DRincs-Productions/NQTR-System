# if in a room there is a different bg (taken in routine) than usual, use this one
default sp_bg_change_room = None

# Change the background image to the current room image. In case sp_bg_change_room is not null use that.
label check_closed_room:
    # Check if the room is closed
    if (cur_room.id in closed_rooms and (closed_rooms[cur_room.id] == None or tm.now_is_between(start=closed_rooms[cur_room.id].tm_start, end=closed_rooms[cur_room.id].tm_stop))):
        if (closed_rooms[cur_room.id].ch_talkobj_dict == None):
            call closed_room_event
        else:
            $ chs1 = closed_rooms[cur_room.id].ch_talkobj_dict
            $ chs2 = getChsInThisLocation(cur_room.id)
            $ res = not bool(chs2)
            # TODO: check if all keys of chs1 are in chs2, in this case res = True
            if (res == True):
                call closed_room_event
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-room
label change_room(room_id = None, close=False):
    # start an event if it exists
    if room_id:
        $ changeRoom(room_id = room_id, rooms = rooms, locations = locations)
    $ sp_bg_change_room = getBgRoomRoutine(cur_routines_location, cur_room.id)
    if (sp_bg_change_room != None):
        scene expression (sp_bg_change_room) as bg
    else:
        scene expression (cur_room.bg) as bg
    call after_spending_time(close = close)
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

# Image of a closed door
define bg_loc = "location/loc-[tm.image_time].webp"
# Is opened in change_room when a room id is in closed rooms
label closed_room_event:
    # Custom code
    # if (cur_room == ...):
        # ...
    scene expression (bg_loc) as bg
    return
