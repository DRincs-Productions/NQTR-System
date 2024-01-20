image pre nqtr_icon talk = Transform("/nqtr_interface/talk.webp", xysize=(gui.sprite_size_x, gui.sprite_size))
image nqtr_icon talk = LayeredImageMask("pre nqtr_icon talk",
    Transform(crop=(gui.sprite_size_padding_x, 0, gui.sprite_size_x, gui.sprite_size_x)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
