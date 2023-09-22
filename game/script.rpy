# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:

    # enable a notify screen
    call enable_notifyEx

    # the first time it opens room navigation screen use after_spending_time
    # for update routine, event...
    call after_spending_time
    # open the room navigation screen
    call screen room_navigation
    return
tion
    return
