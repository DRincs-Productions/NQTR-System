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
    call screen room_navigation

## Error and warming Label

label error_label:
    "ERROR"
    return

label development:
    "In development"
    call screen room_navigation

## Various actions

label order_product:
    mc "OK! Let's see, let's look for a book...."
    mc "Here's R****, for $1. Just the thing for me."
    $ sp_actions.pop('order_product')
    $ stage_memory["alice"].next_quest()
    call screen room_navigation

label add_product:
    $ sp_actions["take_product"] = Action(_("Take product"), "/interface/action-box.webp", label = "take_product", sp_room='terrace')
    call screen room_navigation

label take_product:
    $ sp_actions.pop('take_product')
    $ stage_memory["alice"].next_quest()
    call screen room_navigation

label talk_sleep:
    "zZz zZz ..."
    call screen room_navigation
