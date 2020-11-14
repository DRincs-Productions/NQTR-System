define ch_talk = ""

label wait:
    if(tm.new_hour(1)):
        call check_event
    else:
        "(It's late, you have to go to bed)"
    call screen room_navigation

label after_waiting:
    # aggiornare i dati tipo energia ecc
    # $ Distribution()
    scene expression (cur_room.bg)
    call screen room_navigation

label talk:
    if(ch_talk == ""):
        "ERROR"
        call screen room_navigation
    if(ch_talk == "alice"):
        "hi, I'm [a]"
    call screen room_navigation