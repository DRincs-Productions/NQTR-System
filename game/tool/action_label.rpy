## Actions they do are meant to pass time

label wait_onehour:
    $ wait_hour = 1
    jump wait

label nap:
    call check_block_spendtime

    menu:
        "Nap for 3 hours":
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

## Various actions

label order_product:
    mc "OK! Let's see, let's look for a book...."
    mc "Here's R****, for $1. Just the thing for me."
    $ del sp_actions['order_product']
    $ quests["alice"].next_stage()
    call screen room_navigation

label add_product:
    $ sp_actions["take_product"] = Action(_("Take product"), "/interface/action-box.webp", label_name = "take_product", room='terrace')
    call screen room_navigation

label take_product:
    $ del sp_actions['take_product']
    $ quests["alice"].next_stage()
    call screen room_navigation

label take_key:
    mc "Are these the car keys?! Well... I should try to access the car!"
    $ flags["goout"] = True
    $ del sp_actions['take_key']
    $ quests["ann"].next_stage()
    call screen room_navigation

label talk_sleep:
    "zZz zZz ..."
    menu:
        "Try waking up":
            # will lock the room
            a "[mc]!!!! What are you doing?!!"
            a "Get out of here! Now!"
            $ closed_rooms[cur_room.id] = df_routine["alice_sleep"]
            jump after_wait
        "Leave her alone":
            pass
    call screen room_navigation
