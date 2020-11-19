init:
    transform middle_room:
        size (136, 136)
        on selected_idle:
            yanchor 0 alpha 0.9
        on idle:
            yanchor 0 alpha 0.9
        on hover:
            yanchor 1 alpha 0.9
        on selected_hover:
            yanchor 1 alpha 0.9
    transform middle_action:
        size (120, 120)
        on selected_idle:
            yanchor 0 alpha 0.7
        on idle:
            yanchor 0 alpha 0.7
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
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
    transform small_menu:
        size (80, 80)
        on selected_idle:
            yanchor 0 alpha 0.4
        on idle:
            yanchor 0 alpha 0.4
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0
    transform small_menu_mobile:
        size (100, 100)
        on selected_idle:
            yanchor 0 alpha 0.4
        on idle:
            yanchor 0 alpha 0.4
        on hover:
            yanchor 1 alpha 1.0
        on selected_hover:
            yanchor 1 alpha 1.0

screen room_navigation():
    modal True
    $ i = 0
    # ch in that Location 
    $ chs = checkChLocation(cur_location)
    # More information by hovering the mouse
    $ (x,y) = renpy.get_mouse_pos()

    hbox:
        yalign 0.99
        xalign 0.01
        spacing 2

        for room in rooms:
            $ i += 1

            # If the Locations where I am is the same as the Locations where the room is located
            if (room.id_location == cur_location):
                button xysize (126, 190) action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('change_room')]:
                    has vbox xsize 126 spacing 0
                    frame xysize (126, 140) background None:
                        # Room icon
                        imagebutton:
                            align (0.5, 0.0)
                            idle room.icon
                            selected_idle room.icon + ' a'
                            selected_hover room.icon + ' a'
                            selected room == cur_room focus_mask True at middle_room
                            action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('change_room')]

                        # Check the presence of ch in that room
                        $ there_are_ch = False
                        for ch in chs:
                            # If it is the selected room
                            if room.id == ch.id_room:
                                # I insert hbox only if they are sure that someone is there
                                $ there_are_ch = True

                        if there_are_ch:
                            hbox ypos 73 xalign 0.5 spacing - 30:
                                for ch in chs:
                                    # If it is the selected room
                                    if room.id == ch.id_room:
                                        $ ch_icon = ch_icons.get(ch.ch)
                                        imagebutton idle ch_icon focus_mask True at small_face:
                                            action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('change_room')]

                    # Room name
                    text room.name font 'DejaVuSans.ttf' size 18 drop_shadow [(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2
                key str(i) action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), Jump('change_room')]

    # Actions
    vbox:
        yalign 0.95
        xalign 0.99
        for room in rooms:
            # Adds the button list of possible actions in that room
            if (room == cur_room):
                for act in getActions(room):
                    imagebutton:
                        idle act.icon
                        focus_mask True
                        action [Hide('wait_navigation'), Jump(act.label)]
                        if renpy.variant("pc"):
                            tooltip act.name
                        at middle_action

            # Add talks for each NPC present.
            # TODO: there is no possibility of group talk
            for ch in chs:
                if (room.id == ch.id_room and room == cur_room):
                    frame xysize (110, 110) background None:
                        imagebutton:
                            idle '/interface/action-talk.webp'
                            focus_mask True
                            action [Hide('wait_navigation'), SetVariable('ch_talk', ch.ch), Jump('talk')]
                            at middle_action
                        # inserts the icon of the character who is currently in that room
                        $ ch_icon = ch_icons.get(ch.ch)
                        imagebutton:
                            idle ch_icon
                            focus_mask True
                            at small_face
                            action [Hide('wait_navigation'), SetVariable('ch_talk', ch.ch), Jump('talk')]
                        if renpy.variant("pc"):
                            tooltip _("Talk")

        # Fixed button to wait
        imagebutton:
            idle '/interface/action-wait.webp'
            focus_mask True
            action [Hide('wait_navigation'), Jump('wait_onehour')]
            if renpy.variant("pc"):
                tooltip _("Wait")
            at middle_action

    # Time
    vbox:
        align (0.5, 0.01)
        text "[tm.hour]:00" xalign (0.5) font 'DejaVuSans.ttf' size 60 drop_shadow [(2, 2)]
        text tm.get_weekday_name() xalign (0.5) font 'DejaVuSans.ttf' size 24 drop_shadow [(2, 2)] line_leading -16

    # Tools
    hbox:
        align (0.01, 0.01)
        spacing 2

        imagebutton:
            idle '/interface/menu-options.webp'
            focus_mask True
            action ShowMenu('save')
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Settings")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-user.webp'
            focus_mask True
            action [Hide('wait_navigation'), Jump('development')]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Characters info")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-memo.webp'
            focus_mask True
            if len(quest_current) > 0 :
                action [Hide('wait_navigation'), Show('menu_memo')]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Memo")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-help.webp'
            focus_mask True
            action ShowMenu('help')
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Help")
            else:
                at small_menu_mobile

    hbox:
        align (0.99, 0.01)
        spacing 2

        # Money
        text "$20" xalign (1.0) font 'DejaVuSans.ttf' size 30 drop_shadow [(2, 2)]

        imagebutton:
            idle '/interface/menu-inventory.webp'
            focus_mask True
            action [Hide('wait_navigation'), Jump('development')]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Backpack")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-phone.webp'
            focus_mask True
            action [Hide('wait_navigation'), Jump('development')]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Smartphone")
            else:
                at small_menu_mobile

        imagebutton:
            idle '/interface/menu-map.webp'
            focus_mask True
            action [Hide('wait_navigation'), Jump('development')]
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Map")
            else:
                at small_menu_mobile

    # More information by hovering the mouse
    if renpy.variant("pc"):
        $ text = GetTooltip()
        if text:
            text "[text]":
                xpos x-20
                ypos y-20
                font 'DejaVuSans.ttf' 
                size 18 
                drop_shadow [(2, 2)] 
                outlines [(2, "#000", 0, 1)]
