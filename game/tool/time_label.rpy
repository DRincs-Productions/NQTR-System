define wait_hour = 1

# Check if the time "pass" block has been activated
define block_spendtime_dialogue = _("You can't do it now")
label check_block_spendtime:
    if(bl_values.get("block_spendtime")):
        "[block_spendtime_dialogue]"
        call screen room_navigation
    return

label new_day:
    call check_block_spendtime
    $ tm.new_day()
    # removes expired Commitments
    $ clearExpiredSPRoutine()
    $ clearExpiredSPActions()
    $ checkInactiveStage()
    jump after_wait
    return

label wait:
    call check_block_spendtime
    if(tm.new_hour(wait_hour)):
        if (map_looking == False):
            jump after_wait
    else:
        "(It's late, you have to go to bed)"
    call screen room_navigation

# it is always started after a delay of
label after_wait:
    # this step is to change the background based on the presence of a ch
    $ cur_routines_location = getChsInThisLocation(cur_location.id)
    $ cur_events_location = getEventsInThisLocation(cur_location.id)
    $ sp_bg_change_room = getBgRoomRoutine(cur_routines_location, cur_room.id)
    # removes expired locked rooms
    $ clearClosedRooms()
    # move to change_room is the best way to move to room_navigation
    jump change_room
