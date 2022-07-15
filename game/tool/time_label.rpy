# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#defalut-value
define DEFAULT_WAIT_HOUR = 1
define DEFAULT_HOUR_OF_NEW_DAY = 5
define DEFAULT_BLOCK_SPENDTIME_DIALOGUE = _("You can't do that now")

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day
label new_day(time_of_new_day = DEFAULT_HOUR_OF_NEW_DAY, close=True, is_check_event=True):
    if(not flags["not_can_spend_time"]):
        python:
            tm.new_day()
            # removes expired Commitments
            sp_routine = clearExpiredRoutine(sp_routine, tm)
            actions = clearExpiredActions(actions, tm.day)
            checkInactiveStage()
        call after_spending_time(close = close, is_check_event = is_check_event)
    else:
        "[DEFAULT_BLOCK_SPENDTIME_DIALOGUE]"
        if (close):
            call screen room_navigation
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#wait
label wait(wait_hour=DEFAULT_WAIT_HOUR, close=True, is_check_event=False):
    if(not flags["not_can_spend_time"]):
        if(tm.new_hour(wait_hour)):
            if (not map_open):
                call after_spending_time(close = close, is_check_event = is_check_event)
        else:
            "(It's late, you have to go to bed)"
    else:
        "[DEFAULT_BLOCK_SPENDTIME_DIALOGUE]"
    if (close):
        call screen room_navigation
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#after-spending-time
label after_spending_time(close=True, is_check_event=False, is_check_routines=True):
    if(is_check_routines):
        # this step is to change the background based on the presence of a ch
        $ cur_routines_location = getChsInThisLocation(cur_location.id)
    # check event
    if (is_check_event):
        $ cur_events_location = getEventsInThisLocation(cur_location.id, sp_routine)
        call check_event
    if(isClosedRoom(cur_room.id, closed_rooms, tm)):
        # Change the background image to the current room image.
        call closed_room_event
    else:
        $ sp_bg_change_room = getBgRoomRoutine(cur_routines_location, cur_room.id)
        if (sp_bg_change_room != None):
            scene expression (sp_bg_change_room) as bg
        else:
            scene expression (cur_room.bg) as bg
    if (close):
        call screen room_navigation
    return
