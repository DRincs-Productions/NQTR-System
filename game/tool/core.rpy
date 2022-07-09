label after_load:
    $ tm = updateTimeHandler(tm)
    $ sp_actions = clearExpiredSPActions(sp_actions, tm)
    $ clearExpiredSPRoutine()
    $ updateBL()
    return
