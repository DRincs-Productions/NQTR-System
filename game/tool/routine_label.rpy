# check_event_sp (Commitment): can be deleted.
# check_event_df: and cannot be deleted.
label check_event:

label check_event_sp:
    # I check if there is an event in this room, if so I start the event and then delete it
    if (cur_room.id in cur_events_location.keys()):
        # if I put python: here "call expression" doesn't work
        $ event_room = cur_room.id
        $ ev = cur_events_location[cur_room.id]
        call expression ev.label_event
        if (event_room == cur_room.id):
            # delete the event in cur_events_location
            $ cur_events_location.pop(cur_room.id)
            # delete the event in sp_routine
            python:
                for k, v in sp_routine.items():
                    if (v.id_room == ev.id_room and v.is_event()):
                        sp_routine.pop(k)
        $ del event_room
        $ del ev
        $ renpy.jump("after_wait")

# Check if there are any events to start at that time
# inserted it when you go to sleep but you can put it wherever you want
# the best use is to start fixed events.
label check_event_df:
    # Custom code
    return
