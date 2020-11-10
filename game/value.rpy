define rooms = [
        Room("my_room", "house", _("MC room"), "location myroom"), 
        Room("alice_room", "house", _("Alice room"), "location aliceroom"), 
        Room("bathroom", "house", _("Bathroom"), "location bathroom"), 
        Room("lounge", "house", _("Lounge"), "location lounge"), 
        Room("terrace", "house", _("Terrace"), "location terrace"), 
        Room("ann_room", "house_Ann", _("Ann room"), "location annroom"),
        Room("courtyard", "house_Ann", _("Courtyard"), "location courtyard"), 
    ]
# Commitments of the NCP
define ch_commitments = [
        Commitment("alice", 20, 10, id_location="house", id_room="alice_room"),
        Commitment("alice", 10, 14, id_location="house", id_room="lounge"),
        Commitment("alice", 10, 14, name="school", type="no_week"),
        Commitment("alice", 14, 20, id_location="house", id_room="terrace"),
    ]

define ch_icons = {
        "alice"         : "icon/Alice.webp",
        "ann"           : "icon/Ann.webp",
    }
