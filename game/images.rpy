# rooms
image pre icon myroom = Transform("location/myroom-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon myroom = LayeredImageMask("pre icon myroom",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon aliceroom = Transform("location/aliceroom-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon aliceroom = LayeredImageMask("pre icon aliceroom",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon annroom = Transform("location/annroom-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon annroom = LayeredImageMask("pre icon annroom",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon bathroom = Transform("location/bathroom.webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon bathroom = LayeredImageMask("pre icon bathroom",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon lounge = Transform("location/lounge-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon lounge = LayeredImageMask("pre icon lounge",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon terrace = Transform("location/terrace-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon terrace = LayeredImageMask("pre icon terrace",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon courtyard = Transform("location/courtyard-[tm.timeslot_number].webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon courtyard = LayeredImageMask("pre icon courtyard",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre icon gym = Transform("location/gym.webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image icon gym = LayeredImageMask("pre icon gym",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)

# locations
image pre map home = Transform("/nqtr_interface/home-00.webp", xysize=(gui.sprite_size, gui.sprite_size))
image icon map home = LayeredImageMask("pre map home",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
image pre map gym = Transform("/nqtr_interface/gym.webp", xysize=(gui.sprite_size, gui.sprite_size))
image icon map gym = LayeredImageMask("pre map gym",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)

image pre icon alice = Transform("icon/Alice.webp", xysize=(gui.sprite_elaborate_size, gui.sprite_elaborate_size))
image icon alice = LayeredImageMask("pre icon alice",
    Transform(crop=(0, 0, gui.sprite_elaborate_size, gui.sprite_elaborate_size)),
    mask="sprite mask elaborate",
    foreground="sprite foreground elaborate",
    background="sprite background elaborate" 
)
image icon ann = "icon/Ann.webp"

image bg map = "location/map-[tm.timeslot_number].webp"
image bg nightcity = "location/nightcity.webp"

image bg myroom = "location/myroom-[tm.timeslot_number].webp"
image bg aliceroom = "location/aliceroom-[tm.timeslot_number].webp"
image bg annroom = "location/annroom-[tm.timeslot_number].webp"
image bg bathroom = "location/bathroom.webp"
image bg lounge = "location/lounge-[tm.timeslot_number].webp"
image bg terrace = "location/terrace-[tm.timeslot_number].webp"
image bg courtyard = "location/courtyard-[tm.timeslot_number].webp"
image bg gym = "location/gym.webp"

image bg alice roomsleep = "Alice/roomsleep0A.webp"
image bg alice terrace = "/Alice/terrace0A.webp"
image bg alice terrace talk = "/Alice/terrace0At.webp"

# Action
image pre action alarm = Transform("/nqtr_interface/alarm.webp", xysize=(gui.sprite_size, gui.sprite_size))
image action alarm = LayeredImageMask("pre action alarm",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
image pre action sleep = Transform("/nqtr_interface/sleep.webp", xysize=(gui.sprite_size, gui.sprite_size))
image action sleep = LayeredImageMask("pre action sleep",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
image pre action box = Transform("/nqtr_interface/box.webp", xysize=(gui.sprite_size, gui.sprite_size))
image action box = LayeredImageMask("pre action box",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
image pre action pc = Transform("/nqtr_interface/pc.webp", xysize=(gui.sprite_size, gui.sprite_size))
image action pc = LayeredImageMask("pre action pc",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
