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

screen wait_navigation():
    frame align (.99, .99) xysize (123, 395) background None:
        has vbox:
            spacing 5
        imagebutton idle 'interface wait 10' focus_mask True action [Hide('wait_navigation'), SetVariable('spent_time', 10), Jump('Waiting')] at small_zoom
        imagebutton idle 'interface wait 30' focus_mask True action [Hide('wait_navigation'), SetVariable('spent_time', 30), Jump('Waiting')] at small_zoom
    timer 2.0 action Hide('wait_navigation')

screen room_navigation():
    modal True
    $ i = 0
    hbox:
        yalign 0.99
        xalign 0.01
        spacing 2

        for room in rooms:

            # If the Locations where I am is the same as the Locations where the room is located
            if (room.id_location == cur_location):
                button xysize (126, 190) action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('AfterWaiting')]:
                    has vbox xsize 126 spacing 0
                    frame xysize (126, 140) background None:
                        # Room icon
                        imagebutton align (0.5, 0.0) idle room.icon selected_idle room.icon + ' a' selected_hover room.icon + ' a':
                            selected room == cur_room focus_mask True at middle_zoom
                            action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('AfterWaiting')]

                    # Room name
                    text room.name font 'DejaVuSans.ttf' size 18 drop_shadow [(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2
                key str(i) action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('AfterWaiting')]
