# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#defalut-value
define DEFAULT_WAIT_HOUR = 1
define DEFAULT_HOUR_OF_NEW_DAY = 5
define DEFAULT_BLOCK_SPENDTIME_DIALOGUE = _("You can't do that now")

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day
label new_day(time_of_new_day = DEFAULT_HOUR_OF_NEW_DAY, after_exit=True, is_check_event=True):
    if(not flags["not_can_spend_time"]):
        python:
            tm.new_day()
            # removes expired Commitments
            clearExpiredRoutine(routine, tm)
            clearExpiredActions(actions, tm.day)
            checkInactiveStage(current_stages= current_quest_stages | current_task_stages)
        call after_spending_time(after_exit = after_exit, is_check_event = is_check_event)
    else:
        "[DEFAULT_BLOCK_SPENDTIME_DIALOGUE]"
        if (after_exit):
            call screen room_navigation
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#wait
label wait(wait_hour=DEFAULT_WAIT_HOUR, after_exit=True, is_check_event=False):
    if(not flags["not_can_spend_time"]):
        if(tm.new_hour(wait_hour)):
            if (not map_open):
                call after_spending_time(after_exit = after_exit, is_check_event = is_check_event)
        else:
            "(It's late, you have to go to bed)"
    else:
        "[DEFAULT_BLOCK_SPENDTIME_DIALOGUE]"
    if (after_exit):
        call screen room_navigation
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#after-spending-time
label after_spending_time(after_exit=True, is_check_event=False, is_check_routines=True):
    if(is_check_routines):
        # this step is to change the background based on the presence of a ch
        $ commitments_in_cur_location = getChsInThisLocation(cur_location.id)
    # check event
    if (is_check_event):
        $ cur_events_location = getEventsInThisLocation(cur_location.id, routine)
        call check_event
    if(isClosedRoom(room_id= cur_room.id, closed_rooms= closed_rooms, now_hour= tm.get_hour_number())):
        # Change the background image to the current room image.
        call closed_room_event
    else:
        $ sp_bg_change_room = getBgRoomRoutine(commitments_in_cur_location, cur_room.id)
        if (sp_bg_change_room):
            scene expression (sp_bg_change_room) as bg
        else:
            scene expression (cur_room.bg) as bg
    if (after_exit):
        call screen room_navigation
    return
