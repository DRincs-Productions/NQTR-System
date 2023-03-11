# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:




    ## make check, for event...
    call after_spending_time

    call enable_notifyEx
    call screen room_navigation
    return
