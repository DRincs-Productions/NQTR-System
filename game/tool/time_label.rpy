# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#defalut-value
define DEFAULT_WAIT_HOUR = 1
define DEFAULT_HOUR_OF_NEW_DAY = 5
define DEFAULT_BLOCK_SPENDTIME_DIALOGUE = _("You can't do that now")

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day
label new_day(time_of_new_day = DEFAULT_HOUR_OF_NEW_DAY, is_check_event=True):
    if(not getFlags("not_can_spend_time")):
        python:
            tm.new_day()
            # removes expired Commitments
            clearExpiredRoutine(routine, tm)
            clearExpiredActions(actions, tm.day)
            checkInactiveStage(current_stages= current_quest_stages | current_task_stages)
        call after_spending_time(is_check_event = is_check_event)
    else:
        "[DEFAULT_BLOCK_SPENDTIME_DIALOGUE]"
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#wait
label wait(wait_hour=DEFAULT_WAIT_HOUR, is_check_event=True):
    if(not getFlags(flag_id = "not_can_spend_time")):
        if(tm.new_hour(wait_hour)):
            if (not map_open):
                call after_spending_time(is_check_event = is_check_event)
        else:
            "(It's late, you have to go to bed)"
    else:
        "[DEFAULT_BLOCK_SPENDTIME_DIALOGUE]"
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#after-spending-time
label after_spending_time(is_check_event=False, is_check_routines=True):
    if(is_check_routines):
        # this step is to change the background based on the presence of a ch
        $ commitments_in_cur_location = getChsInThisLocation(cur_location.id)
    # check event
    if (is_check_event):
        $ cur_events_location = getEventsInThisLocation(cur_location.id, routine)
        call check_event
    call set_background
    return
