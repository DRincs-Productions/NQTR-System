define gui.nqtr_icon_small = convert_to_int(gui.sprite_size - (100 * gui.dr_multiplicateur))
define gui.nqtr_icon_small_crop = convert_to_int(- 50 * gui.dr_multiplicateur)

image pre nqtr_icon options = Transform("/nqtr_interface/options.webp", xysize=(gui.nqtr_icon_small, gui.nqtr_icon_small))
image nqtr_icon options = LayeredImageMask("pre nqtr_icon options",
    Transform(crop=(gui.nqtr_icon_small_crop, gui.nqtr_icon_small_crop, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre nqtr_icon characters info = Transform("/nqtr_interface/user.webp", xysize=(gui.nqtr_icon_small, gui.nqtr_icon_small))
image nqtr_icon characters info = LayeredImageMask("pre nqtr_icon characters info",
    Transform(crop=(gui.nqtr_icon_small_crop, gui.nqtr_icon_small_crop, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre nqtr_icon memo = Transform("/nqtr_interface/memo.webp", xysize=(gui.nqtr_icon_small, gui.nqtr_icon_small))
image nqtr_icon memo = LayeredImageMask("pre nqtr_icon memo",
    Transform(crop=(gui.nqtr_icon_small_crop, gui.nqtr_icon_small_crop, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre nqtr_icon help = Transform("/nqtr_interface/help.webp", xysize=(gui.nqtr_icon_small, gui.nqtr_icon_small))
image nqtr_icon help = LayeredImageMask("pre nqtr_icon help",
    Transform(crop=(gui.nqtr_icon_small_crop, gui.nqtr_icon_small_crop, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre nqtr_icon inventory = Transform("/nqtr_interface/inventory.webp", xysize=(gui.sprite_size, gui.sprite_size))
image nqtr_icon inventory = LayeredImageMask("pre nqtr_icon inventory",
    Transform(crop=(0, 0, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre nqtr_icon phone = Transform("/nqtr_interface/phone.webp", xysize=(gui.nqtr_icon_small, gui.nqtr_icon_small))
image nqtr_icon phone = LayeredImageMask("pre nqtr_icon phone",
    Transform(crop=(gui.nqtr_icon_small_crop, gui.nqtr_icon_small_crop, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre nqtr_icon map = Transform("/nqtr_interface/map.webp", xysize=(gui.nqtr_icon_small, gui.nqtr_icon_small))
image nqtr_icon map = LayeredImageMask("pre nqtr_icon map",
    Transform(crop=(gui.nqtr_icon_small_crop, gui.nqtr_icon_small_crop, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background" 
)
image pre nqtr_icon wait = Transform("/nqtr_interface/wait.webp", xysize=(gui.nqtr_icon_small, gui.nqtr_icon_small))
image nqtr_icon wait = LayeredImageMask("pre nqtr_icon wait",
    Transform(crop=(gui.nqtr_icon_small_crop, gui.nqtr_icon_small_crop, gui.sprite_size, gui.sprite_size)),
    mask="sprite mask",
    foreground="sprite foreground",
    background="sprite background"
)
