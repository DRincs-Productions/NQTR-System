define config.log = "log.txt"

label after_load:
    $ update_flags()
    python:
        from pythonpackages.nqtr.action import clearExpiredActions
        from pythonpackages.nqtr.routine import clearExpiredRoutine
        from pythonpackages.nqtr.routine import getEventsInThisLocation
        from pythonpackages.nqtr.routine import getChsInThisLocation

        updateTimeHandler(tm)
        clear_expired_actions(actions, tm.day)
        clear_expired_routine(routine, tm)
        cur_events_location = characters_events_in_current_location(cur_location.id, routine, tm)
        commitments_in_cur_location = characters_commitment_in_current_location(cur_location.id, routine | df_routine, tm)
        updateQuestsLevels()
    return

init python:
    def myrollback():
        ui.add(renpy.Keymap(rollback=If(renpy.get_screen('menu_memo'), NullAction(), Rollback())))

    config.overlay_functions.append(myrollback)

