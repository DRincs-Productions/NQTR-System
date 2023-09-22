init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.conversation import Conversation

# habitual routine
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_routine = {
    "alice_sleep" : Commitment(
        conversations = [
            Conversation(
                name="talk_alice_sleep",
                label_name="talk_sleep",
                characters=a,
                conversation_background = None,
            ),
        ],
        hour_start=20, hour_stop=10,
        location_id="house", room_id="alice_room",
        background ="bg alice roomsleep",
    ),
    # alice_go_school have more priority than alice_read, because it is before in the dictionary
    "alice_go_school" : Commitment(
        characters=a, # characters can be a string or a list of strings
        hour_start=10, hour_stop=14,
        location_id="school",
        disabled="weekend",
    ),
    "alice_read" : Commitment(
        conversations = [
            Conversation(
                name="talk_alice_read",
                characters=a,
                conversation_background ="bg alice terrace talk"
            ),
        ],
        hour_start=10, hour_stop=20,
        location_id="house", room_id="terrace",
        background ="bg alice terrace",
    ),
}
