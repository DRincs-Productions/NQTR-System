define config.log = "log.txt"

label after_load:
    # renpy-utility-lib
    call update_current_flags(update_dictionary = True)

    # nqtr
    python:
        # timeHandler update: if you update TimeHandler settings into a new version, you can use this function to update the old save files.
        updateTimeHandler(tm)
        # clear the expired actions and routine
        from pythonpackages.nqtr.action import clear_expired_actions
        from pythonpackages.nqtr.routine import clear_expired_routine
        clear_expired_actions(actions, tm.day)
        clear_expired_routine(routine, tm)
        # recheck the character's events and commitments in current location
        from pythonpackages.nqtr.routine import characters_events_in_current_location
        from pythonpackages.nqtr.routine import characters_commitment_in_current_location
        cur_events_location = characters_events_in_current_location(cur_location.id, routine, tm)
        commitments_in_cur_location = characters_commitment_in_current_location(cur_location.id, routine | df_routine, tm, flags)
        # update the quest levels, if ypu add a new stage in the quest, you can use this function to start the new stage
        update_quests_levels()
    return
