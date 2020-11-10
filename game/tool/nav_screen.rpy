init:
    transform middle_zoom:
        size (136, 136)
        on selected_idle:
            yanchor 0 alpha 1.0
        on idle:
            yanchor 0 alpha 1.0
        on hover:
            yanchor 1 alpha 0.9
        on selected_hover:
            yanchor 1 alpha 0.9
    transform small_face:
        size (60, 60)
        on selected_idle:
            yanchor 0 alpha 1.0
        on idle:
            yanchor 0 alpha 1.0
        on hover:
            yanchor 1 alpha 0.93
        on selected_hover:
            yanchor 1 alpha 0.93


screen room_navigation():
    modal True
    $ i = 0
    hbox:
        yalign 0.99
        xalign 0.01
        spacing 2
        # ch in that Location 
        $ chs = checkChLocation(cur_location)

        for room in rooms:
            $ i += 1

            # If the Locations where I am is the same as the Locations where the room is located
            if (room.id_location == cur_location):
                button xysize (126, 190) action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('AfterWaiting')]:
                    has vbox xsize 126 spacing 0
                    frame xysize (126, 140) background None:
                        # Room icon
                        imagebutton align (0.5, 0.0) idle room.icon selected_idle room.icon + ' a' selected_hover room.icon + ' a':
                            selected room == cur_room focus_mask True at middle_zoom
                            action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('AfterWaiting')]

                        # Check the presence of ch in that room
                        $ val = False
                        for ch in chs:
                            # If it is the selected room
                            if room.id == ch.id_room: # TODO: check the time
                                # I insert hbox only if they are sure that someone is there
                                $ val = True

                        if val == True:
                            hbox ypos 73 xalign 0.5 spacing - 30:
                                for ch in chs:
                                    # If it is the selected room
                                    if room.id == ch.id_room: # TODO: check the time
                                        $ ch_icon = ch_icons.get(ch.ch)
                                        imagebutton idle ch_icon focus_mask True at small_face:
                                            action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('AfterWaiting')]

                    # Room name
                    text room.name font 'DejaVuSans.ttf' size 18 drop_shadow [(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2
                key str(i) action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('AfterWaiting')]

    # Actions
    hbox:
        align (.99, .99)
        # Fixed button to wait
        button xysize (136, 190) action [Hide('wait_navigation'), Jump('new_hour')]:
            has vbox xsize 136 spacing 0
            frame xysize (136, 140) background None:
                imagebutton idle '/interface/wait.webp' selected_hover '/interface/wait.webp':
                    align (0.5, 0.0) focus_mask True action [Hide('wait_navigation'), Jump('new_hour')] at middle_wait
            text _("WAIT") font 'DejaVuSans.ttf' size 18 drop_shadow [(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2
