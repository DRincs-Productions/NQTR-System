label after_load:
    $ tm = updateTimeHandler(tm)
    $ sp_actions = clearExpiredActions(sp_actions, tm)
    $ clearExpiredSPRoutine(sp_routine, tm)
    $ flags = updateFlags(flags, flag_keys)
    return
