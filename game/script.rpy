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
    $ quests["alice"].start()
    $ quests["ann"].start()

    ## make check, for event...
    call after_spending_time

    call enable_notifyEx
    call screen room_navigation
    return
