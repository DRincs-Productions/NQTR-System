init python:
    from pythonpackages.nqtr.navigation import is_closed_room
    from pythonpackages.nqtr.routine import commitment_background
    from pythonpackages.nqtr.action import current_button_actions, current_picture_in_background_actions
    from pythonpackages.nqtr.conversation_fun import current_button_conversations, current_picture_in_background_conversations

screen room_navigation():
    modal True
    # More information by hovering the mouse
    $ (x,y) = renpy.get_mouse_pos()

    # Map
    if (map_open and cur_map_id):
        use map(maps, cur_map_id)

        for location in locations:
            # If the Map where I am is the same as the Map where the room is located
            use location_button(location)

    else:
        # Action and Room with Picture in background
        for room in rooms:
            if room.is_picture_in_background and not room.is_hidden(flags = flags):
                use room_picture_in_background(room)
            # Adds the button list of possible actions in that room
            if (cur_room and room.id == cur_room.id and not room.id in closed_rooms):
                for act in current_picture_in_background_actions(actions= actions | df_actions, room = room, now_hour = tm.hour , current_day = tm.day, tm = tm, flags = flags):
                    use action_picture_in_background(act)
            # Talk
            # Adds a talk for each ch (NPC) and at the talk interval adds the icon for each secondary ch
            for conversation, comm in current_picture_in_background_conversations(commitments_in_cur_location, room, cur_room):
                use conversation_picture_in_background(conversation, comm.conversation_background(conversation.character))

        # Rooms
        use room_button_list(rooms, commitments_in_cur_location)

        # Normal Actions (with side button)
        vbox:
            yalign 0.95
            xalign 0.99
            spacing 2
            for room in rooms:
                # Adds the button list of possible actions in that room
                if (cur_room and room.id == cur_room.id):
                    for act in current_button_actions(actions= actions | df_actions, room = room, now_hour = tm.hour , current_day = tm.day, tm = tm, flags = flags):
                        use action_button(act)

                # Talk
                # Adds a talk for each ch (NPC) and at the talk interval adds the icon for each secondary ch
                for conversation, comm in current_button_conversations(commitments_in_cur_location, room, cur_room):
                    use conversation_button(conversation, comm.conversation_background(conversation.character))

            # Fixed button to wait
            use wait_button()

    # Time
    use time_text(tm, show_wait_button = map_open)

    # Tools
    hbox:
        align (0.01, 0.01)
        spacing 2

        imagebutton:
            idle nqtr_menu_icon_options
            focus_mask True
            action ShowMenu('save')
            if renpy.variant("pc"):
                tooltip _("Settings")
            at dr_button_menu_transform

        if renpy.has_label("open_characters_info"):
            imagebutton:
                idle nqtr_menu_icon_characters_info
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = "open_characters_info"),
                ]
                if renpy.variant("pc"):
                    tooltip _("Characters info")
                at dr_button_menu_transform

        if len(current_quest_stages) > 0 :
            imagebutton:
                idle nqtr_menu_memo
                focus_mask True
                action [
                    SetVariable('cur_task_menu', ""),
                    SetVariable('cur_quest_menu', ""),
                    Show('menu_memo'),
                ]
                if renpy.variant("pc"):
                    tooltip _("Memo")
                at dr_button_menu_transform

        imagebutton:
            idle nqtr_menu_icon_help
            focus_mask True
            action ShowMenu('help')
            if renpy.variant("pc"):
                tooltip _("Help")
            at dr_button_menu_transform

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
                idle nqtr_menu_icon_inventory
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = "open_inventory"),
                ]
                if renpy.variant("pc"):
                    tooltip _("Backpack")
                at dr_button_menu_transform

        if renpy.has_label("open_smartphone"):
            imagebutton:
                idle nqtr_menu_icon_phone
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = "open_smartphone"),
                ]
                if renpy.variant("pc"):
                    tooltip _("Smartphone")
                at dr_button_menu_transform

        imagebutton:
            idle nqtr_menu_icon_map
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = "open_map"),
            ]
            if renpy.variant("pc"):
                tooltip _("Map")
            at dr_button_menu_transform

    # More information by hovering the mouse
    if renpy.variant("pc"):
        $ text = GetTooltip()
        if text:
            text "[text]":
                xpos x-20
                ypos y-20
                size gui.dr_little_text_size 
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
    elif not renpy.has_label(label_name_to_call):
        $ log_error("label_name_to_call: " + label_name_to_call + " not found", renpy.get_filename_line())
    else:
        $ renpy.call(label_name_to_call)
    call set_background_nqtr
    call screen room_navigation
    $ log_error("thera is a anomaly in room_navigation. value: " + label_name_to_call, renpy.get_filename_line())
    jump after_return_from_room_navigation
