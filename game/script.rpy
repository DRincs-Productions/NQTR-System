# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Player")
define a = Character("Alice")
define an = Character("Ann")


# The game starts here.

label start:
    $ block_goout_dialogue = _("To get out you have to take the car keys, (talk to Alice)")

    $ cur_location = "house"
    $ cur_room = rooms[0]
    $ prev_room = rooms[5]
    $ updateBL()
    $ stage_memory["alice"].start()
    $ stage_memory["ann"].start()

    ## call screen room_navigation
    call after_wait

    return
