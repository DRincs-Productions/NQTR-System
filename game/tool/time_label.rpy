define wait_hour = 1

# Check if the time "pass" block has been activated
define block_spendtime_dalogue = _("You can't do it now")
label check_block_spendtime:
    if(bl_values.get("block_spendtime")):
        "[block_spendtime_dalogue]"
        call screen room_navigation
    return

label new_day:
    call check_block_spendtime
    $ tm.new_day()
    # removes expired Commitments
    $ clearExpiredSPRoutine()
    $ clearExpiredSPActions()
    jump after_wait
    return

label wait:
    call check_block_spendtime
    if(tm.new_hour(wait_hour)):
        jump after_wait
    else:
        "(It's late, you have to go to bed)"
    call screen room_navigation

# it is always started after a delay of
label after_wait:
    # this step is to change the background based on the presence of a ch
    $ cur_routines_location = getChsInThisLocation(cur_location)
    $ sp_bg_change_room = getBgRoomRoutine(cur_routines_location, cur_room.id)
    # start an event if it exists
    call check_event
    # move to change_room is the best way to move to room_navigation
    jump change_room

# Check if there are any events to start at that time
# inserted it when you go to sleep but you can put it wherever you want
label check_event:
    # Custom code
    return
