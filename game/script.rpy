# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Player")
define a = Character("Alice")
define an = Character("Ann")


# The game starts here.

label start:
    $ block_goout_dialogue = _("To get out you have to take the car keys, (talk to Alice)")

    call change_room(room_id = "my_room")
    $ prev_room = rooms[5]
    $ flags = updateFlags(flags, flag_keys)
    python:
        if(quests["alice"].start() == False):
            log_error("The quest alice has not started", renpy.get_filename_line())
        if(quests["ann"].start() == False):
            log_error("The quest ann has not started", renpy.get_filename_line())

    ## make check, for event...
    call after_spending_time

    call enable_notifyEx
    call screen room_navigation
    return
