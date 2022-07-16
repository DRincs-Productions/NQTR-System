label after_load:
    $ tm = updateTimeHandler(tm)
    $ actions = clearExpiredActions(actions, tm.day)
    $ sp_routine = clearExpiredRoutine(sp_routine, tm)
    $ flags = updateFlags(flags, flag_keys)
    $ cur_events_location = getEventsInThisLocation(cur_location.id, sp_routine)
    $ cur_routines_location = getChsInThisLocation(cur_location.id)
    return
