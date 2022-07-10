# are the routines of the CHs in the current place
# it is changed after waiting for some time or when moving from one location to another
default cur_routines_location = None

# possible events in the current location
default cur_events_location = None

# special routine of the NCP
# they are added after completing missions or for some other reason.
# if there is another commitment in the default routine at the same time, it will be "overwritten"
default sp_routine = {}

# default routine of the NCP
# do not have a deadline
# ATTENTION I for I have excluded the search of events in df_routine (because it does not see a their practical use here)
# events are only in sp_routine
define df_routine = {
        "alice_sleep"       :   Commitment(chs={"alice" : TalkObject(label_talk="talk_sleep")}, tm_start=20, tm_stop=10, id_location="house", id_room="alice_room", bg="bg alice roomsleep"),
        "alice_lounge"      :   Commitment(chs={"alice" : TalkObject(bg_talk=None)}, tm_start=10, tm_stop=14, id_location="house", id_room="lounge", bg=None),
        "alice_go_school"   :   Commitment(chs={"alice" : TalkObject(bg_talk=None)}, tm_start=10, tm_stop=14, name="school", type="no_week", bg=None),
        "alice_read"        :   Commitment(chs={"alice" : TalkObject(bg_talk="bg alice terrace talk")}, tm_start=14, tm_stop=20, id_location="house", id_room="terrace", bg="bg alice terrace"),
}
