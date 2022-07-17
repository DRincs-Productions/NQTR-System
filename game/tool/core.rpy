label after_load:
    $ updateTimeHandler(tm)
    $ clearExpiredActions(actions, tm.day)
    $ clearExpiredRoutine(routine, tm)
    $ flags = updateFlags(flags, flag_keys)
    $ cur_events_location = getEventsInThisLocation(cur_location.id, routine)
    $ commitments_in_cur_location = getChsInThisLocation(cur_location.id)
    $ updateQuestsLevels()
    return
