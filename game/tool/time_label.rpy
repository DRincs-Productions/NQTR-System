define DEFAULT_WAIT_HOUR = 1
define DEFAULT_HOUR_OF_NEW_DAY = 1

# Check if the time "pass" block has been activated
define block_spendtime_dialogue = _("You can't do that now")

label new_day(time_of_new_day = DEFAULT_HOUR_OF_NEW_DAY, close=True, is_check_event=True):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day """
    if(not flags["not_can_spend_time"]):
        python:
            tm.new_day()
            # removes expired Commitments
            sp_routine = clearExpiredRoutine(sp_routine, tm)
            actions = clearExpiredActions(actions, tm.day)
            checkInactiveStage()
        if (is_check_event):
            call check_event
        call after_spending_time(close = close)
    if (close):
        call screen room_navigation
    else:
        return
    return

label wait(wait_hour=DEFAULT_WAIT_HOUR, close=True, is_check_event=False):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#wait """
    if(not flags["not_can_spend_time"]):
        if(tm.new_hour(wait_hour)):
            if (map_open == False):
                call after_spending_time(close = close)
        else:
            "(It's late, you have to go to bed)"
        if (is_check_event):
            call check_event
    if (close):
        call screen room_navigation
    else:
        return

# it is always started after a delay of
label after_spending_time(close=True):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#after-spending-time """
    # this step is to change the background based on the presence of a ch
    $ cur_routines_location = getChsInThisLocation(cur_location.id)
    $ cur_events_location = getEventsInThisLocation(cur_location.id, sp_routine)
    $ sp_bg_change_room = getBgRoomRoutine(cur_routines_location, cur_room.id)
    # removes expired locked rooms
    $ closed_rooms = clearClosedRooms(closed_rooms, tm)
    # move to change_room is the best way to move to room_navigation
    call change_room(close = close)
    return
