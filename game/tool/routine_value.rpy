init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.action_talk import TalkObject

# are the routines of the CHs in the current place
# it is changed after waiting for some time or when moving from one location to another
default commitments_in_cur_location = {}

# possible events in the current location
default cur_events_location = {}

# dictionary editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default routine = {}

# habitual routine
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_routine = {
}
