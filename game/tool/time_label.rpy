label new_day:
    $ tm.new_day()
    call check_event
    # removes expired Commitments
    $ update_sp_routine()
    return

label check_event:
    # Custom code
    return
