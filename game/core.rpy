define config.log = "log.txt"

label after_load:
    $ update_flags()
    python:
        from pythonpackages.nqtr.action import clear_expired_actions
        from pythonpackages.nqtr.routine import clear_expired_routine
        from pythonpackages.nqtr.routine import characters_events_in_current_location
        from pythonpackages.nqtr.routine import characters_commitment_in_current_location

        updateTimeHandler(tm)
        clear_expired_actions(actions, tm.day)
        clear_expired_routine(routine, tm)
        cur_events_location = characters_events_in_current_location(cur_location.id, routine, tm)
        commitments_in_cur_location = characters_commitment_in_current_location(cur_location.id, routine | df_routine, tm)
        update_quests_levels()
    return
