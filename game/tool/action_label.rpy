## Actions they do are meant to pass time

label nap:
    menu:
        "Nap for 3 hours":
            call wait(3)
        "Sleep":
            jump sleep
        "Return":
            pass
    return

label sleep:
    menu:
        "What time do you want to set the alarm?"
        "[DEFAULT_HOUR_OF_NEW_DAY]:00":
            call new_day(is_check_event=True)
        "7:00":
            call new_day(time_of_new_day = 7, is_check_event=True)
        "9:00":
            call new_day(time_of_new_day = 9, is_check_event=True)
        "Return":
            pass
    return

## Development Label

label development:
    "In development"
    return

label development_characters_info:
    "In development in another repo: {a=https://github.com/DRincs-Productions/DS-toolkit}DS toolkit{/a}"
    return

label development_inventory:
    "In development in another repo: {a=https://github.com/DRincs-Productions/Inventory-System-toolkit}Inventory System{/a}"
    return

## Various actions

label order_product:
    mc "OK! Let's see, let's look for a book...."
    mc "Here's R****, for $1. Just the thing for me."
    $ del actions['order_product']
    $ quests["alice"].nextStage()
    return

label add_product:
    $ actions["take_product"] = Act(name = _("Take product"), button_icon = "/interface/action-box.webp", label_name = "take_product", rooms=['terrace'])
    return

label take_product:
    $ del actions['take_product']
    $ quests["alice"].nextStage()
    return

label take_key:
    mc "Are these the car keys?! Well... I should try to access the car!"
    $ flags["goout"] = True
    $ del actions['take_key']
    $ quests["ann"].nextStage()
    return

label talk_sleep:
    "zZz zZz ..."
    menu:
        "Try waking up":
            # will lock the room
            a "[mc]!!!! What are you doing?!!"
            a "Get out of here! Now!"
            $ closed_rooms[cur_room.id] = df_routine["alice_sleep"]
            jump after_spending_time
        "Leave her alone":
            pass
    return
