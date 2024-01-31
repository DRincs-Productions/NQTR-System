image pre nqtr_icon talk = Transform("/nqtr_interface/talk.webp", xysize=(gui.nqtr_icon_small, gui.nqtr_icon_small))
image nqtr_icon talk = LayeredImageMask("pre nqtr_icon talk",
    Transform(crop=(gui.nqtr_icon_small_crop, gui.nqtr_icon_small_crop, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
