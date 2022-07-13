label after_load:
    $ tm = updateTimeHandler(tm)
    $ actions = clearExpiredActions(actions, tm.day)
    $ sp_routine = clearExpiredRoutine(sp_routine, tm)
    $ flags = updateFlags(flags, flag_keys)
    return
