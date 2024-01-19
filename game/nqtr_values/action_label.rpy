## Actions they do are meant to pass time

menu nap:
    "Nap for 3 hours":
        call wait(3)
        return
    "Sleep":
        jump sleep
        return
    "Return":
        return

menu sleep:
    "What time do you want to set the alarm?"
    "[tm.hour_of_new_day]:00":
        call new_day(is_check_event=True)
        return
    "7:00":
        call new_day(time_of_new_day = 7, is_check_event=True)
        return
    "9:00":
        call new_day(time_of_new_day = 9, is_check_event=True)
        return
    "Return":
        return

## Various actions

label order_product:
    mc "OK! Let's see, let's look for a book...."
    mc "Here's R****, for $1. Just the thing for me."
    $ del actions['order_product']
    $ quest_next_stage(id = "alice")
    return

label add_product:
    $ actions["take_product"] = Act(name = _("Take product"), button_icon = "action box", label_name = "take_product", room_ids=['terrace'])
    return

label take_product:
    $ del actions['take_product']
    $ quest_next_stage(id = "alice")
    return

label take_key:
    mc "Are these the car keys?! Well... I should try to access the car!"
    $ set_flags("goout", True)
    $ del actions['take_key']
    $ quest_next_stage(id = "ann")
    return

menu talk_sleep:
    "zZz zZz ..."
    "Try waking up":
        # will lock the room
        a "[mc]!!!! What are you doing?!!"
        a "Get out of here! Now!"
        $ closed_rooms[cur_room.id] = df_routine["alice_sleep"]
        call after_spending_time
        return
    "Leave her alone":
        return

label alice_talk_menu:
    if(current_conversation_character == a):
        mc "Hi [a]"
        a "Hi, can you tell me something?"
    else:
        "Now is busy test later."

    call talk_menu

## Development Label

label open_smartphone:
    "In development"
    return

label open_characters_info:
    "In development in another repo: {a=https://github.com/DRincs-Productions/DS-toolkit}DS toolkit{/a}"
    return

label open_inventory:
    "In development in another repo: {a=https://github.com/DRincs-Productions/Inventory-System-toolkit}Inventory System{/a}"
    return
