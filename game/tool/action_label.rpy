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
        "[DEFAULT_HOUR_OF_NEW_DAY]:00":
            call new_day(is_check_event=True)
        "7:00":
            call new_day(time_of_new_day = 7, is_check_event=True)
        "9:00":
            call new_day(time_of_new_day = 9, is_check_event=True)
        "Return":
            pass
    jump after_spending_time

## Error and warming Label

label error_label:
    "ERROR"
    return

label development:
    "In development"
    call screen room_navigation

label development_characters_info:
    "In development in another repo: {a=https://github.com/DRincs-Productions/DS-toolkit}DS toolkit{/a}"
    call screen room_navigation

label development_inventory:
    "In development in another repo: {a=https://github.com/DRincs-Productions/Inventory-System-toolkit}Inventory System{/a}"
    call screen room_navigation
