screen menu_tile(title):

    frame:
        area (150, 70, 350, 50)
        background None
        text title:
            color gui.accent_color
            size gui.name_text_size

screen close_button(screen_name):

    # button for closure
    imagebutton:
        align (0.95, 0.05)
        idle '/nqtr_interface/button/close_idle.webp'
        action [
            Hide(screen_name),
        ]
        if renpy.variant("pc"):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_mobile
