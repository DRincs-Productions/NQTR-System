init python:
    from pythonpackages.nqtr.navigation import get_room_by_id

# if in a room there is a different bg (taken in routine) than usual, use this one
default sp_bg_change_room = None
# Image of a closed door
define bg_loc = "location/loc-[tm.timeslot_number].webp"
## Check if mc can come out
define block_goout_dialogue = _("Now is not the time to go outside")

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-room
label change_room(room_id = None):
    if room_id:
        $ new_room = get_room_by_id(room_id = room_id, rooms = rooms)
        if new_room is None:
            $ log_error("Room with id [room_id] not found", renpy.get_filename_line())
            return
        python:
            prev_room = cur_room
            cur_room = new_room
            del new_room
    if cur_location.id != cur_room.location_id:
        python:
            new_location = get_location_by_id(location_id = cur_room.location_id, locations = locations)
            prev_location = cur_location
            cur_location = new_location
            del new_location
    call after_spending_time(is_check_event=True)
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#change-location
label change_location(location_id = None, close_map = True):
    if location_id:
        python:
            new_location = get_location_by_id(location_id = location_id, locations = locations)
            prev_location = cur_location
            cur_location = new_location
            del new_location
    call change_room(cur_location.external_room_id)
    call close_map
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Navigation-and-Map#go-previous-room
label go_previous_room:
    python:
        temp_room = cur_room
        cur_room = prev_room
        prev_room = temp_room
        del temp_room
    return

## Open the map or close the map
label open_map:
    if(not get_flags("goout")):
        "[block_goout_dialogue]"
        return

    if not cur_location:
        call change_room(room_id = cur_room.location_id)
    
    $ cur_map_id = cur_location.map_id

    if (not map_open):
        call set_image_map
        $ map_open = True
        call screen room_navigation
        return

## Close the map
label close_map:
    python:
        map_open = False
    return

# Is opened in change_room when a room id is in closed rooms
label closed_room_event:
    if renpy.has_label("closed_room_event_custom"):
        call closed_room_event_custom
    scene expression (bg_loc) as bg
    return

label set_image_map:
    scene expression maps[cur_map_id].background as bg
    return
