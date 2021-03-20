image icon myroom = "location/myroom-icon.webp"
image icon aliceroom = "location/aliceroom-icon.webp"
image icon annroom = "location/annroom-icon.webp"
image icon bathroom = "location/bathroom-icon.webp"
image icon lounge = "location/lounge-icon.webp"
image icon terrace = "location/terrace-icon.webp"
image icon courtyard = "location/courtyard-icon.webp"

image icon myroom a = im.MatrixColor("location/myroom-icon.webp", im.matrix.brightness(-0.5))
image icon aliceroom a = im.MatrixColor("location/aliceroom-icon.webp", im.matrix.brightness(-0.5))
image icon annroom a = im.MatrixColor("location/annroom-icon.webp", im.matrix.brightness(-0.5))
image icon bathroom a = im.MatrixColor("location/bathroom-icon.webp", im.matrix.brightness(-0.5))
image icon lounge a = im.MatrixColor("location/lounge-icon.webp", im.matrix.brightness(-0.5))
image icon terrace a = im.MatrixColor("location/terrace-icon.webp", im.matrix.brightness(-0.5))
image icon courtyard a = im.MatrixColor("location/courtyard-icon.webp", im.matrix.brightness(-0.5))

image icon map home = "/interface/map-home.webp"

image icon map home a = im.MatrixColor("/interface/map-home.webp", im.matrix.brightness(-0.5))

image icon alice = "Alice/icon.webp"
image icon ann = "Ann/icon.webp"

image bg map = "location/map-[tm.image_time].webp"

image bg myroom = "location/myroom-[tm.image_time].webp"
image bg aliceroom = "location/aliceroom-[tm.image_time].webp"
image bg annroom = "location/annroom-[tm.image_time].webp"
image bg bathroom = "location/bathroom.webp"
image bg lounge = "location/lounge-[tm.image_time].webp"
image bg terrace = "location/terrace-[tm.image_time].webp"
image bg courtyard = "location/courtyard-[tm.image_time].webp"

image bg alice roomsleep = Composite( (1920, 1080),
    (0, 0), "/Alice/roomsleep0.webp",
    (0, 0), "/Alice/roomsleep0A.webp")
image bg alice terrace = Composite( (1920, 1080),
    (0, 0), "/Alice/terrace0.webp",
    (0, 0), "/Alice/terrace0A.webp")
image bg alice terrace talk = Composite( (1920, 1080),
    (0, 0), "/Alice/terrace0.webp",
    (0, 0), "/Alice/terrace0At.webp")
