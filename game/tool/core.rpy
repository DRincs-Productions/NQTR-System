define config.log = "log.txt"

label after_load:
    python:
        from pythonpackages.nqtr.action import clearExpiredActions
        from pythonpackages.nqtr.routine import clearExpiredRoutine
        from pythonpackages.nqtr.routine import getEventsInThisLocation
        from pythonpackages.nqtr.routine import getChsInThisLocation

        updateTimeHandler(tm)
        clearExpiredActions(actions, tm.day)
        clearExpiredRoutine(routine, tm)
        flags = updateFlags(flags, flag_keys)
        cur_events_location = getEventsInThisLocation(cur_location.id, routine)
        commitments_in_cur_location = getChsInThisLocation(cur_location.id, routine | df_routine, tm)
        updateQuestsLevels()
    return

init python:
    def myrollback():
        ui.add(renpy.Keymap(rollback=If(renpy.get_screen('menu_memo'), NullAction(), Rollback())))

    config.overlay_functions.append(myrollback)

