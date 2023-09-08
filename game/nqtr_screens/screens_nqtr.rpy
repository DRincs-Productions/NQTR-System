init python:
    from pythonpackages.nqtr.navigation import is_closed_room
    from pythonpackages.nqtr.routine import commitment_background
    from pythonpackages.nqtr.action import current_button_actions, current_picture_in_background_actions

screen room_navigation():
    modal True
    $ i = 0
    # More information by hovering the mouse
    $ (x,y) = renpy.get_mouse_pos()

    # Map
    if (map_open and cur_map_id):
        use map(maps, cur_map_id)

        for location in locations:
            # If the Map where I am is the same as the Map where the room is located
            use location_button(location)

    else:
        # Rooms
        hbox:
            yalign 0.99
            xalign 0.01
            spacing 2

            for room in rooms:
                $ i += 1

                # Check the presence of ch in that room
                $ there_are_ch = False
                for comm in commitments_in_cur_location.values():
                    # If it is the selected room
                    if comm != None and room.id == comm.room_id:
                        # I insert hbox only if they are sure that someone is there
                        $ there_are_ch = True

                use room_button(room, cur_room, i, there_are_ch)

        # Action wich Picture in background
        for room in rooms:
            # Adds the button list of possible actions in that room
            if (cur_room and room.id == cur_room.id and not room.id in closed_rooms):
                for act in current_picture_in_background_actions(actions= actions | df_actions, room = room, now_hour = tm.hour , current_day = tm.day, tm = tm, flags = flags):
                    use action_picture_in_background(act)

        # Normal Actions (with side button)
        vbox:
            yalign 0.95
            xalign 0.99
            for room in rooms:
                # Adds the button list of possible actions in that room
                if (cur_room and room.id == cur_room.id):
                    for act in current_button_actions(actions= actions | df_actions, room = room, now_hour = tm.hour , current_day = tm.day, tm = tm, flags = flags):
                        use action_button(act)

                # Talk
                # Adds a talk for each ch (NPC) and at the talk interval adds the icon for each secondary ch
                for comm in commitments_in_cur_location.values():
                    if (cur_room and comm and room.id == comm.room_id and room.id == cur_room.id):
                        # Insert in talk for every ch, main in that room
                        for ch_id, talk_obj in comm.ch_talkobj_dict.items():
                            if (talk_obj):
                                use action_talk_button(ch_id, talk_obj, comm.conversation_background(ch_id))

            # Fixed button to wait
            use wait_button()

    # Time
    use time_text(tm, show_wait_button = map_open)

    # Tools
    hbox:
        align (0.01, 0.01)
        spacing 2

        imagebutton:
            idle '/nqtr_interface/menu-options.webp'
            focus_mask True
            action ShowMenu('save')
            if renpy.variant("pc"):
                at small_menu
                tooltip _("Settings")
            else:
                at small_menu_mobile

        if renpy.has_label("open_characters_info"):
            imagebutton:
                idle '/nqtr_interface/menu-user.webp'
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = "open_characters_info"),
                ]
                if renpy.variant("pc"):
                    at small_menu
                    tooltip _("Characters info")
                else:
                    at small_menu_mobile

        if len(current_quest_stages) > 0 :
            imagebutton:
                idle '/nqtr_interface/menu-memo.webp'
                focus_mask True
                action [
                    Show('menu_memo'),
                ]
                if renpy.variant("pc"):
                    at small_menu
                    tooltip _("Memo")
                else:
                    at small_menu_mobile

        imagebutton:
            idle '/nqtr_interface/menu-help.webp'
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
        text "$20":
            align(1.0, 0.5)
            size gui.interface_text_size
            drop_shadow [(2, 2)]

        if renpy.has_label("open_inventory"):
            imagebutton:
                idle '/nqtr_interface/menu-inventory.webp'
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = "open_inventory"),
                ]
                if renpy.variant("pc"):
                    at small_menu
                    tooltip _("Backpack")
                else:
                    at small_menu_mobile

        if renpy.has_label("open_smartphone"):
            imagebutton:
                idle '/nqtr_interface/menu-phone.webp'
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = "open_smartphone"),
                ]
                if renpy.variant("pc"):
                    at small_menu
                    tooltip _("Smartphone")
                else:
                    at small_menu_mobile

        imagebutton:
            idle '/nqtr_interface/menu-map.webp'
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = "open_map"),
            ]
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
                size gui.little_text_size 
                drop_shadow [(2, 2)] 
                outlines [(2, "#000", 0, 1)]

label set_background_nqtr:
    if (not map_open):
        if(is_closed_room(room_id= cur_room.id, closed_rooms= closed_rooms, now_hour= tm.hour, tm = tm)):
            # Change the background image to the current room image.
            call closed_room_event
        else:
            $ sp_bg_change_room = commitment_background(commitments_in_cur_location, cur_room.id)
            call set_room_background(sp_bg_change_room)
    return

label set_room_background(sp_bg_change_room = ""):
    if (not isNullOrEmpty(sp_bg_change_room)):
        call set_background(sp_bg_change_room)
    else:
        call set_background(cur_room.background)
    return

# making calls safely:
# Why? Because if I use Call("label") in sleep mode from the room_navigation
# and in the "label" I use "return" an almost all cases the game will end.
label after_return_from_room_navigation(label_name_to_call = ""):
    if isNullOrEmpty(label_name_to_call):
        $ log_error("label_name_to_call is empty", renpy.get_filename_line())
    else:
        $ renpy.call(label_name_to_call)
    call set_background_nqtr
    call screen room_navigation
    $ log_error("thera is a anomaly in room_navigation. value: " + label_name_to_call, renpy.get_filename_line())
    jump after_return_from_room_navigation
