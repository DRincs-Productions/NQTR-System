label check_event:
    if renpy.has_label("check_event_custom"):
        call check_event_custom

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
    return
