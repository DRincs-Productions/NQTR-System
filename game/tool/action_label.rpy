## Actions they do are meant to pass time

label nap:
    menu:
        "Nap for 3 hours":
            call wait(3)
        "Sleep":
            jump sleep
        "Return":
            pass
    call screen room_navigation

label sleep:
    menu:
        "What time do you want to set the alarm?"
        "[tm.hour_of_new_day]:00":
            call new_day(close=False, is_check_event=True)
        "7:00":
            call new_day(new_day_hour = 7, is_check_event=True)
        "9:00":
            call new_day(new_day_hour = 9, is_check_event=True)
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
    $ del actions['order_product']
    $ quests["alice"].next_stage()
    call screen room_navigation

label add_product:
    $ actions["take_product"] = Action(name = _("Take product"), button_icon = "/interface/action-box.webp", label_name = "take_product", rooms=['terrace'])
    call screen room_navigation

label take_product:
    $ del actions['take_product']
    $ quests["alice"].next_stage()
    call screen room_navigation

label take_key:
    mc "Are these the car keys?! Well... I should try to access the car!"
    $ flags["goout"] = True
    $ del actions['take_key']
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
