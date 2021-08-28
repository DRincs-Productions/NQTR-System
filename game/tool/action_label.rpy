## Actions they do are meant to pass time

label wait_onehour:
    $ wait_hour = 1
    jump wait

label nap:
    call check_block_spendtime

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
    jump after_wait

## Error and warming Label

label error_label:
    "ERROR"
    return

label development:
    "In development"
    call screen room_navigation
