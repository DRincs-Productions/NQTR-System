label new_hour:
    if(tm.new_hour(1)):
        call check_event
    else:
        "(It's late, you have to go to bed)"
    call screen room_navigation

label new_day:
    $ tm.new_day()
    call check_event
    return

label after_waiting:
    scene expression (cur_room.bg)
    call screen room_navigation

label check_event:
    # Custom code
    return
