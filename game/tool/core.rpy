label after_load:
    $ updateTimeHandler()
    $ df_actions = clearExpiredSPActions(df_actions, tm)
    $ clearExpiredSPRoutine()
    $ updateBL()
    return
