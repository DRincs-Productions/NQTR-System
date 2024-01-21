image pre nqtr_icon talk = Transform("/nqtr_interface/talk.webp", xysize=(gui.sprite_size, gui.sprite_size))
image nqtr_icon talk = LayeredImageMask("pre nqtr_icon talk",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
