# are the routines of the CHs in the current place
# it is changed after waiting for some time or when moving from one location to another
default commitments_in_cur_location = {}

# possible events in the current location
default cur_events_location = {}

# special routine of the NCP
# they are added after completing missions or for some other reason.
# if there is another commitment in the default routine at the same time, it will be "overwritten"
default sp_routine = {}

# default routine of the NCP
# do not have a deadline
# ATTENTION I for I have excluded the search of events in df_routine (because it does not see a their practical use here)
# events are only in sp_routine
define df_routine = {
        "alice_sleep"       :   Commitment(ch_talkobj_dict={"alice" : TalkObject(label_name="talk_sleep")}, tm_start=20, tm_stop=10, location_id="house", room_id="alice_room", bg="bg alice roomsleep"),
        "alice_lounge"      :   Commitment(ch_talkobj_dict={"alice" : TalkObject(bg=None)}, tm_start=10, tm_stop=14, location_id="house", room_id="lounge", bg=None),
        "alice_go_school"   :   Commitment(ch_talkobj_dict={"alice" : TalkObject(bg=None)}, tm_start=10, tm_stop=14, location_id="school", type="no_week", bg=None),
        "alice_read"        :   Commitment(ch_talkobj_dict={"alice" : TalkObject(bg="bg alice terrace talk")}, tm_start=14, tm_stop=20, location_id="house", room_id="terrace", bg="bg alice terrace"),
}
