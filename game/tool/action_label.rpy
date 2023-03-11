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
