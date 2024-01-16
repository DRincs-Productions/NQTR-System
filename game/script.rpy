# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -1:
    default a_name = "Test"
    define mc = Character("Player")
    define a = Character("[a_name]", icon = "icon alice")
    define an = Character("Ann", icon = "icon ann")


# The game starts here.

label start:
    $ block_goout_dialogue = _("To get out you have to take the car keys, (talk to Alice)")

    call change_room(room_id = "my_room")
    $ prev_room = rooms[5]
    if(not quest_start(id = "alice")):
        $ log_error("The quest alice has not started", renpy.get_filename_line())
    if(not quest_start(id = "ann")):
        $ log_error("The quest ann has not started", renpy.get_filename_line())

    # enable a notify screen
    call enable_notifyEx

    # the first time it opens room navigation screen use after_spending_time
    # for update routine, event...
    call after_spending_time
    "Hello, this is a test of NQTR-System."
    $ a_name = "Alice"
    # open the room navigation screen
    call screen room_navigation
    return
