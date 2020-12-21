# if in a room there is a different bg (taken in routine) than usual, use this one
default sp_bg_change_room = None

# Change the background image to the current room image. In case sp_bg_change_room is not null use that.
label change_room:
    if (sp_bg_change_room != None):
        scene expression (sp_bg_change_room)
    else:
        scene expression (cur_room.bg)
    call screen room_navigation
