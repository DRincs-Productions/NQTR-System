screen wait_button(small = False):
    imagebutton:
        idle '/nqtr_interface/action-wait.webp'
        focus_mask True
        action [
            Call("after_return_from_room_navigation", label_name_to_call = "wait"),
        ]
        if renpy.variant("pc"):
            tooltip _("Wait")
        if small:
            at nqtr_button_location_transform
        else:
            at nqtr_button_action_transform

screen character_icon_screen(icon):
    if icon:
        imagebutton:
            idle icon
            focus_mask True
            action []
            at dr_small_face_transform

screen time_text(tm, show_wait_button = False):
    hbox:
        align (0.5, 0.01)
        vbox:
            align (0.5, 0.01)
            text "[tm.hour]:00":
                xalign (0.5)
                size gui.nqtr_hour_text_size
                drop_shadow [(2, 2)]
            text tm.weekday_name:
                xalign (0.5)
                size gui.dr_normal_text_size
                drop_shadow [(2, 2)]
                line_leading -16

        if (show_wait_button):
            # Fixed button to wait
            use wait_button(small = True)

screen action_button(act):
    imagebutton:
        idle act.button_icon
        hover act.button_icon_selected
        focus_mask True
        action [
            Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
        ]
        if renpy.variant("pc"):
            tooltip act.name
        at nqtr_button_action_transform

screen action_picture_in_background(act):
    imagebutton:
        align (act.xalign, act.yalign)
        idle act.picture_in_background
        hover act.picture_in_background_selected
        focus_mask True
        action [
            Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
        ]
        if renpy.variant("pc"):
            tooltip act.name
        at nqtr_button_action_picture_transform

screen action_talk_button(conversation, background):
    if not conversation.is_hidden(flags = flags, check_if_has_icon = False):
        frame:
            xysize (gui.nqtr_button_action_size, gui.nqtr_button_action_size)
            background None

            imagebutton:
                align (0.5, 0.0)
                if conversation.is_button:
                    idle conversation.button_icon
                    hover conversation.button_icon_selected
                else:
                    idle gui.default_talk_button_icon
                focus_mask True
                action [
                    SetVariable('talk_ch', conversation.character),
                    SetVariable('talk_image', background),
                    Call("after_return_from_room_navigation", label_name_to_call = conversation.label_name),
                ]
                at nqtr_button_action_transform
                if renpy.variant("pc"):
                    tooltip _("Talk")

            use character_icon_screen(conversation.character_icon)

screen location_button(location):
    if (location.map_id == cur_map_id and not location.is_hidden(flags = flags)):
        vbox:
            align (location.yalign, location.xalign)
            imagebutton:
                if location.is_picture_in_background:
                    idle location.picture_in_background
                    selected_idle location.picture_in_background_selected
                    selected_hover location.picture_in_background_selected
                selected location == cur_location
                sensitive not location.is_hidden(flags)
                focus_mask True
                action [
                    SetVariable('cur_location', location),
                    Call("after_return_from_room_navigation", label_name_to_call = "change_location"),
                ]
                at nqtr_button_location_transform

            # Locations name
            text location.name:
                size gui.dr_little_text_size
                drop_shadow [(2, 2)]
                xalign 0.5
                text_align 0.5
                line_leading 0
                line_spacing -2

screen map_button(map_id, map, align_value, rotation):
    if not map.is_hidden(flags = flags, check_if_has_icon = False):
        hbox:
            align align_value
            imagebutton:
                idle "gui triangular_button"
                focus_mask True
                sensitive not map.is_disabled(flags)
                action [
                    SetVariable('cur_map_id', map_id), 
                    Call("after_return_from_room_navigation", label_name_to_call = "set_image_map"),
                ]
                if renpy.variant("pc"):
                    tooltip map.name
                at nqtr_button_map_transform(rotation)

screen map(maps, cur_map_id):
    $ map_id_north = maps[cur_map_id].map_id_north
    $ map_id_south = maps[cur_map_id].map_id_south
    $ map_id_east = maps[cur_map_id].map_id_east
    $ map_id_west = maps[cur_map_id].map_id_west

    # North map
    if not isNullOrEmpty(map_id_north):
        use map_button(map_id = map_id_north, map = maps[map_id_north], align_value = (0.5, 0.1), rotation = 270)
    # South map
    if not isNullOrEmpty(map_id_south):
        use map_button(map_id = map_id_south, map = maps[map_id_south], align_value = (0.5, 0.99), rotation = 90)
    # West map
    if not isNullOrEmpty(map_id_west):
        use map_button(map_id = map_id_west, map = maps[map_id_west], align_value = (0.001, 0.5), rotation = 180)
    # East map
    if not isNullOrEmpty(map_id_east):
        use map_button(map_id = map_id_east, map = maps[map_id_east], align_value = (0.999, 0.5), rotation = 0)

screen room_button(room, cur_room, i, find_ch = False):
    # If the Locations where I am is the same as the Locations where the room is located
    if (room.location_id == cur_location.id and room.is_button != None and not room.is_hidden(flags)):
        vbox:
            frame:
                xysize (gui.nqtr_button_action_size, gui.nqtr_button_action_size + gui.dr_little_text_size)
                background None

                # Room icon
                imagebutton:
                    align (0.5, 0.0)
                    if room.is_button:
                        idle room.button_icon
                    selected_idle room.button_icon_selected
                    selected_hover room.button_icon_selected
                    selected (True if cur_room and cur_room.id == room.id else False)
                    sensitive not room.is_disabled(flags)
                    focus_mask True
                    action [
                        SetVariable('prev_room', cur_room),
                        SetVariable('cur_room', room),
                        Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
                    ]
                    at nqtr_button_room_transform

                if find_ch:
                    hbox:
                        xalign 0.5
                        yalign 0.99

                        for comm in commitments_in_cur_location.values():
                            # If it is the selected room
                            if room.id == comm.room_id:
                                use character_icon_screen(comm.character_icon)
            # Room name
            text room.name:
                size gui.dr_little_text_size
                drop_shadow [(2, 2)]
                xalign 0.5
                text_align 0.5
                line_leading 0
                line_spacing -2
        key str(i) action [
            SetVariable('prev_room', cur_room),
            SetVariable('cur_room', room),
            Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
        ]
