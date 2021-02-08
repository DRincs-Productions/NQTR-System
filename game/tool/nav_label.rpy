# if in a room there is a different bg (taken in routine) than usual, use this one
default sp_bg_change_room = None

# Change the background image to the current room image. In case sp_bg_change_room is not null use that.
label change_room:
    # I check if there is an event in this room, if so I start the event and then delete it
    if (cur_room.id in cur_events_location.keys()):
        # if I put python: here renpy.call() doesn't work
        $ event_room = cur_room.id
        $ ev = cur_events_location[cur_room.id]
        $ renpy.call(ev.label_event)
        if (event_room == cur_room.id):
            # delete the event in cur_events_location
            $ cur_events_location.pop(cur_room.id)
            # delete the event in sp_routine
            python:
                for k, v in sp_routine.items():
                    if (v.id_room == ev.id_room):
                        sp_routine.pop(k)
        $ del event_room
        $ del ev
        $ renpy.call("after_wait")

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
