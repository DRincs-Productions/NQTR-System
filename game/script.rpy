# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    $ cur_location = "house"
    $ cur_room = rooms[4]
    $ prev_room = rooms[5]

    call screen room_navigation

    return
