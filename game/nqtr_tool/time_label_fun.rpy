init python:
    from pythonpackages.nqtr.action import clear_expired_actions
    from pythonpackages.nqtr.routine import clear_expired_routine
    from pythonpackages.nqtr.routine import characters_events_in_current_location
    from pythonpackages.nqtr.routine import characters_commitment_in_current_location

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#defalut-value
# pressing the hold button will increase the time of:
define DEFAULT_WAIT_HOUR = 1
# using the default new day function the time of the next day will be:
define DEFAULT_BLOCK_SPENDTIME_DIALOGUE = _("You can't do that now")

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day
label new_day(time_of_new_day = None, is_check_event=True):
    if(not get_flags("not_can_spend_time")):
        python:
            tm.new_day()
            # removes expired Commitments
            clear_expired_routine(routine, tm)
            clear_expired_actions(actions, tm.day)
            check_inactive_stage(current_stages= current_quest_stages | current_task_stages)
            if (time_of_new_day is not None):
                tm.hour = time_of_new_day
            else:
                tm.hour= tm.hour_of_new_day
        call after_spending_time(is_check_event = is_check_event)
    else:
        "[DEFAULT_BLOCK_SPENDTIME_DIALOGUE]"
    return

# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#wait
label wait(wait_hour=DEFAULT_WAIT_HOUR, is_check_event=True):
    if(not get_flags(flag_id = "not_can_spend_time")):
        if(tm.new_hour(wait_hour)):
            if (not map_open):
                call after_spending_time(is_check_event = is_check_event)
        else:
            "(It's late, you have to go to bed)"
    else:
        "[DEFAULT_BLOCK_SPENDTIME_DIALOGUE]"
    return

# is a label that is called always after spending time, 
# or into special cases before checking the event, or routine...
# this label is used to update all the variables that are used in the time system
label after_spending_time(is_check_event=False, is_check_routines=True):
    call update_current_flags
    if(is_check_routines):
        # this step is to change the background based on the presence of a ch
        $ commitments_in_cur_location = characters_commitment_in_current_location(cur_location.id, routine | df_routine, tm, flags)
    # check event
    if (is_check_event):
        $ cur_events_location = characters_events_in_current_location(cur_location.id, routine, tm, flags)
        call check_event
    call set_background_nqtr
    return
