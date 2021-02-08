# if in a room there is a different bg (taken in routine) than usual, use this one
default sp_bg_change_room = None

# Change the background image to the current room image. In case sp_bg_change_room is not null use that.
label change_room:
    # start an event if it exists
    call check_event

    if (sp_bg_change_room != None):
        scene expression (sp_bg_change_room)
    else:
        scene expression (cur_room.bg)
    call screen room_navigation

## Check if mc can come out
define block_goout_dialogue = _("Now is not the time to go outside")
label check_goout:
    if(bl_values.get("goout") == False):
        "[block_goout_dialogue]"
        call screen room_navigation
    return

## Open the map
label open_map:
    call check_goout

    call development
    return
