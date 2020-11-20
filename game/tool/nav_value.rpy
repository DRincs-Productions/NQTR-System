define rooms = [
        Room("my_room", "house", _("MC room"), "icon myroom", "bg myroom", actions = ["sleep","nap",]), 
        Room("alice_room", "house", _("[a] room"), "icon aliceroom", "bg aliceroom"), 
        Room("bathroom", "house", _("Bathroom"), "icon bathroom", "bg bathroom"), 
        Room("lounge", "house", _("Lounge"), "icon lounge", "bg lounge"), 
        Room("terrace", "house", _("Terrace"), "icon terrace", "bg terrace"), 
        Room("ann_room", "house_Ann", _("Ann room"), "icon annroom", "bg annroom"),
        Room("courtyard", "house_Ann", _("Courtyard"), "icon courtyard", "bg courtyard"), 
    ]

define ch_icons = {
        "alice"     : "icon/Alice.webp",
        "ann"       : "icon/Ann.webp",
    }

# Id of the task selected in the menu
default cur_task_menu = ""
# quest level based on the task selected in the menu
default cur_quest_menu = ""
