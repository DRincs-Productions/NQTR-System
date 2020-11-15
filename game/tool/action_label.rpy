define ch_talk = ""

label wait:
    if(tm.new_hour(1)):
        call check_event
    else:
        "(It's late, you have to go to bed)"
    call screen room_navigation

label error_label:
    "ERROR"
    return

label after_waiting:
    # aggiornare i dati tipo energia ecc
    # $ Distribution()
    scene expression (cur_room.bg)
    call screen room_navigation

label nap:
    menu:
        "Nap for 3 hour":
            $ tm.new_hour(3)
        "Sleep":
            jump sleep
        "Return":
            pass
    call screen room_navigation

label sleep:
    menu:
        "What time do you want to set the alarm?"
        "[tm.hour_new_day]:00":
            call new_day
        "7:00":
            call new_day
            $ tm.new_hour(7-tm.hour_new_day)
        "9:00":
            call new_day
            $ tm.new_hour(9-tm.hour_new_day)
        "Return":
            pass
    call screen room_navigation

label talk:
    if(ch_talk == ""):
        call error_label
        call screen room_navigation
    if(ch_talk == "alice"):
        a "hi, I'm [a]"
    call screen room_navigation
