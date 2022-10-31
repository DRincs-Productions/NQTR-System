define config.log = "log.txt"

label after_load:
    $ updateTimeHandler(tm)
    $ clearExpiredActions(actions, tm.day)
    $ clearExpiredRoutine(routine, tm)
    $ flags = updateFlags(flags, flag_keys)
    $ cur_events_location = getEventsInThisLocation(cur_location.id, routine)
    $ commitments_in_cur_location = getChsInThisLocation(cur_location.id)
    $ updateQuestsLevels()
    return

init python:
    def myrollback():
        ui.add(renpy.Keymap(rollback=If(renpy.get_screen('menu_memo'), NullAction(), Rollback())))

    config.overlay_functions.append(myrollback)

