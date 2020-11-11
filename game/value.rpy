define rooms = [
        Room("my_room", "house", _("MC room"), "icon myroom", "bg myroom"), 
        Room("alice_room", "house", _("Alice room"), "icon aliceroom", "bg aliceroom"), 
        Room("bathroom", "house", _("Bathroom"), "icon bathroom", "bg bathroom"), 
        Room("lounge", "house", _("Lounge"), "icon lounge", "bg lounge"), 
        Room("terrace", "house", _("Terrace"), "icon terrace", "bg terrace"), 
        Room("ann_room", "house_Ann", _("Ann room"), "icon annroom", "bg annroom"),
        Room("courtyard", "house_Ann", _("Courtyard"), "icon courtyard", "bg courtyard"), 
    ]
# default routine of the NCP
# do not have a deadline
define df_routine = [
        Commitment("alice", 20, 10, id_location="house", id_room="alice_room"),
        Commitment("alice", 10, 14, id_location="house", id_room="lounge"),
        Commitment("alice", 10, 14, name="school", type="no_week"),
        Commitment("alice", 14, 20, id_location="house", id_room="terrace"),
    ]

define ch_icons = {
        "alice"         : "icon/Alice.webp",
        "ann"           : "icon/Ann.webp",
    }
