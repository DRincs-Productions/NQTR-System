define ch_talk = None
define wait_hour = 1
# Check if the time "pass" block has been activated
define block_spendtime_dalogue = _("You can't do it now")
label check_block_spendtime:
    if(bl_values.get("block_spendtime")):
        "[block_spendtime_dalogue]"
        call screen room_navigation
    return

label wait_onehour:
    $ wait_hour = 1
    jump wait

label wait:
    call check_block_spendtime

    if(tm.new_hour(wait_hour)):
        call check_event
    else:
        "(It's late, you have to go to bed)"
    call screen room_navigation

label error_label:
    "ERROR"
    return

label change_room:
    scene expression (cur_room.bg)
    call screen room_navigation

label nap:
    menu:
        "Nap for 3 hour":
            $ wait_hour = 3
            jump wait
        "Sleep":
            jump sleep
        "Return":
            pass
    call screen room_navigation

label sleep:
    call check_block_spendtime

    menu:
        "What time do you want to set the alarm?"
        "[tm.hour_new_day]:00":
            call new_day
            call check_event
        "7:00":
            call new_day
            call check_event
            $ tm.new_hour(7-tm.hour_new_day)
        "9:00":
            call new_day
            call check_event
            $ tm.new_hour(9-tm.hour_new_day)
        "Return":
            pass
    call screen room_navigation

label talk:
    if(ch_talk == None):
        call error_label
        call screen room_navigation
    if(ch_talk == "alice"):
        a "hi, I'm [a]"
    call screen room_navigation

label take_object:
    $ removeSpAction("take_object")
    call screen room_navigation

label development:
    "In development"
    call screen room_navigation
