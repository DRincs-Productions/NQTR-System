# if in a room there is a different bg (taken in routine) than usual, use this one
default sp_bg_change_room = None

# Change the background image to the current room image. In case sp_bg_change_room is not null use that.
label change_room:
    # Check if the room is closed
    if (cur_room.id in closed_rooms and (closed_rooms[cur_room.id] == None or tm.now_is_between(start=closed_rooms[cur_room.id].tm_start, end=closed_rooms[cur_room.id].tm_stop))):
        if (closed_rooms[cur_room.id].chs == None):
            jump closed_room_event
        else:
            $ chs1 = closed_rooms[cur_room.id].chs
            $ chs2 = getChsInThisLocation(cur_room.id)
            $ res = not bool(chs2)
            # TODO: check if all keys of chs1 are in chs2, in this case res = True
            if (res == True):
                jump closed_room_event

    # start an event if it exists
    call check_event

    if (sp_bg_change_room != None):
        scene expression (sp_bg_change_room) as bg
    else:
        scene expression (cur_room.bg) as bg
    call screen room_navigation

## Check if mc can come out
define block_goout_dialogue = _("Now is not the time to go outside")
label check_goout:
    if(bl_values.get("goout") == False):
        "[block_goout_dialogue]"
        call screen room_navigation
    return

## Open the map or close the map
label open_map:
    call check_goout

    $ cur_location = locations[cur_room.id_location]
    scene expression map_images[cur_location.key_map] as bg

    if (map_open == False):
        $ map_open = True
        call screen room_navigation
## Close the map
label close_map:
    python:
        for room in rooms:
            if(room.id == cur_location.id_externalroom):
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
    call screen room_navigation
    return
