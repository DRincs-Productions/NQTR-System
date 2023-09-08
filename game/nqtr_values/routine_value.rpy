init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.action_talk import TalkObject

# habitual routine
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_routine = {
    "alice_sleep" : Commitment(
        ch_talkobj_dict={
            "alice" : TalkObject(
                name="talk_alice_sleep",
                label_name="talk_sleep",
                conversation_background = None,
            ),
        },
        hour_start=20, hour_stop=10,
        location_id="house", room_id="alice_room",
        background ="bg alice roomsleep",
    ),
    "alice_lounge" : Commitment(
        hour_start=10, hour_stop=14,
        location_id="house", room_id="lounge",
    ),
    "alice_go_school" : Commitment(
        hour_start=10, hour_stop=14,
        location_id="school", tag="no_week",
    ),
    "alice_read" : Commitment(
        ch_talkobj_dict={
            "alice" : TalkObject(
                name="talk_alice_read",
                conversation_background ="bg alice terrace talk"
            ),
        },
        hour_start=14, hour_stop=20,
        location_id="house", room_id="terrace",
        background ="bg alice terrace",
    ),
}
