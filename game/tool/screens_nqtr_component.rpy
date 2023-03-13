screen wait_button(small = False):
    imagebutton:
        if small:
            xysize (300, 300)
        idle '/interface/action-wait.webp'
        focus_mask True
        action [
            Call("after_return_from_room_navigation", label_name_to_call = "wait"),
        ]
        if renpy.variant("pc"):
            tooltip _("Wait")
        at middle_action

screen time_text(tm, show_wait_button = False):
    hbox:
        align (0.5, 0.01)
        vbox:
            align (0.5, 0.01)
            text "[tm.hour]:00":
                xalign (0.5)
                size gui.hour_text_size
                drop_shadow [(2, 2)]
            text tm.get_weekday_name():
                xalign (0.5)
                size gui.normal_text_size
                drop_shadow [(2, 2)]
                line_leading -16

        if (show_wait_button):
            # Fixed button to wait
            use wait_button(small = True)
