# special routine of the NCP
# they are added after completing missions or for some other reason.
# if there is another commitment in the default routine at the same time, it will be "overwritten"
default sp_routine = {}

# default routine of the NCP
# do not have a deadline
define df_routine = {
        "alice_sleep"       :   Commitment("alice", 20, 10, id_location="house", id_room="alice_room"),
        "alice_lounge"      :   Commitment("alice", 10, 14, id_location="house", id_room="lounge"),
        "alice_go_school"   :   Commitment("alice", 10, 14, name="school", type="no_week"),
        "alice_take_sun"    :   Commitment("alice", 14, 20, id_location="house", id_room="terrace"),
    }
