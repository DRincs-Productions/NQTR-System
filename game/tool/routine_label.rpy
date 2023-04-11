# check_event_sp (Commitment): can be deleted.
# check_event_df: and cannot be deleted.
label check_event:

# ## ATTENTION:
# if the mc has not moved, the system delete the event (resolves any loops)
# se si vuole degli eventi fissi usare check_event_df
# if you want the event to be started only once and then deleted
# at the end of the label insert:
# return
# if you want the event to be repeated every time you go to that room
# at the end of the label insert:
# call change_room
# if you want the event to be repeated only once, but then it is repeated after waiting some time or changing location_id
# at the end of the label insert:
# $ del cur_events_location[cur_room.id]    # cur_room.id: i.e. the id of the room where the event is triggered
# call change_room

label check_event_sp:
    # I check if there is an event in this room, if so I start the event and then delete it
    if (cur_room.id in cur_events_location.keys()):
        # if I put python: here "call expression" doesn't work
        $ event_room = cur_room.id
        $ ev = cur_events_location[cur_room.id]
        call expression ev.event_label_name
        python:
            if (event_room == cur_room.id):
                # delete the event in cur_events_location
                del cur_events_location[cur_room.id]
                # delete the event in routine
                sp_routine_to_del = []
                for k, v in routine.items():
                    if (v.room_id == ev.room_id and v.is_event):
                        sp_routine_to_del.append(k)
                for k in sp_routine_to_del:
                    del routine[k]
                del sp_routine_to_del
        $ del event_room
        $ del ev
        call after_spending_time(is_check_event=True)

# Check if there are any events to start at that time
# inserted it when you go to sleep but you can put it wherever you want
# the best use is to start fixed events.
label check_event_df:
    # Custom code
    return
