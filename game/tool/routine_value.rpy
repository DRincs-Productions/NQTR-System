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
        "alice_sleep"       :   Commitment(ch_talkobj_dict={"alice" : TalkObject(label_name="talk_sleep")}, tm_start=20, tm_stop=10, location_id="house", room_id="alice_room", bg="bg alice roomsleep"),
        "alice_lounge"      :   Commitment(tm_start=10, tm_stop=14, location_id="house", room_id="lounge", bg=None),
        "alice_go_school"   :   Commitment(tm_start=10, tm_stop=14, location_id="school", type="no_week", bg=None),
        "alice_read"        :   Commitment(ch_talkobj_dict={"alice" : TalkObject(bg="bg alice terrace talk")}, tm_start=14, tm_stop=20, location_id="house", room_id="terrace", bg="bg alice terrace"),
}
