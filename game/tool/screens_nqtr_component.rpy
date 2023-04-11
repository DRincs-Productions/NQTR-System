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
            text tm.weekday_name:
                xalign (0.5)
                size gui.normal_text_size
                drop_shadow [(2, 2)]
                line_leading -16

        if (show_wait_button):
            # Fixed button to wait
            use wait_button(small = True)

screen action_button(act, show_picture_in_background = False):
    if show_picture_in_background:
        imagebutton:
            align (act.xalign, act.yalign)
            if act.is_picture_in_background: # for logs
                idle act.picture_in_background
                hover act.picture_in_background_selected
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
            ]
            if renpy.variant("pc"):
                tooltip act.name
            at middle_action_is_in_room
    else:
        imagebutton:
            if act.is_button: # for logs
                idle act.button_icon
                hover act.button_icon_selected
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
            ]
            if renpy.variant("pc"):
                tooltip act.name
            at middle_action

screen action_talk_button(ch_id, talk_obj, background):
    if not talk_obj.isHidden(flags = flags, check_if_has_icon = False):
        frame:
            xysize (120, 120)
            background None

            imagebutton:
                if talk_obj.is_button:
                    idle talk_obj.button_icon
                    hover talk_obj.button_icon_selected
                else:
                    idle gui.default_talk_button_icon
                focus_mask True
                action [
                    SetVariable('talk_ch', ch_id),
                    SetVariable('talk_image', background),
                    Call("after_return_from_room_navigation", label_name_to_call = talk_obj.label_name),
                ]
                at middle_action
            # inserts the icon of the character who is currently in that room
            # TODO: for now insert only the icon of the main ch_id, I have to insert also the icon of the other secondary ch_id
            if (ch_id in ch_icons):
                imagebutton:
                    idle ch_icons.get(ch_id)
                    focus_mask True
                    at small_face
                    action [
                        SetVariable('talk_ch', ch_id),
                        SetVariable('talk_image', background),
                        Call("after_return_from_room_navigation", label_name_to_call = talk_obj.label_name),
                    ]
            if renpy.variant("pc"):
                tooltip _("Talk")

screen location_button(location):
    if (location.map_id == cur_map_id and not location.isHidden(flags = flags)):
        vbox:
            align (location.yalign, location.xalign)
            imagebutton:
                if location.is_picture_in_background:
                    idle location.picture_in_background
                    selected_idle location.picture_in_background_selected
                    selected_hover location.picture_in_background_selected
                selected location == cur_location
                sensitive not location.isHidden(flags)
                focus_mask True
                action [
                    SetVariable('cur_location', location),
                    Call("after_return_from_room_navigation", label_name_to_call = "change_location"),
                ]
                at small_map

            # Locations name
            text location.name:
                size gui.little_text_size
                drop_shadow [(2, 2)]
                xalign 0.5
                text_align 0.5
                line_leading 0
                line_spacing -2

screen map_button(map_id, map, align_value, rotation):
    if not map.isHidden(flags = flags, check_if_has_icon = False):
        hbox:
            align align_value
            imagebutton:
                idle "gui triangular_button"
                focus_mask True
                sensitive not map.isDisabled(flags)
                action [
                    SetVariable('cur_map_id', map_id), 
                    Call("after_return_from_room_navigation", label_name_to_call = "set_image_map"),
                ]
                if renpy.variant("pc"):
                    tooltip map.name
                at middle_map(rotation)

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
    if (room.location_id == cur_location.id and room.is_button != None and not room.isHidden(flags)):
        button:
            xysize (126, 190)
            action [
                SetVariable('prev_room', cur_room),
                SetVariable('cur_room', room),
                Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
            ]
            has vbox xsize 126 spacing 0

            frame:
                xysize (126, 140)
                background None

                # Room icon
                imagebutton:
                    align (0.5, 0.0)
                    if room.is_button:
                        idle room.button_icon
                    selected_idle room.button_icon_selected
                    selected_hover room.button_icon_selected
                    selected (True if cur_room and cur_room.id == room.id else False)
                    sensitive not room.isDisabled(flags)
                    focus_mask True
                    action [
                        SetVariable('prev_room', cur_room),
                        SetVariable('cur_room', room),
                        Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
                    ]
                    at middle_room

                if find_ch:
                    hbox:
                        ypos 73
                        xalign 0.5
                        spacing - 30

                        for comm in commitments_in_cur_location.values():
                            # If it is the selected room
                            if room.id == comm.room_id:
                                for ch_icon in comm.getChIcons(ch_icons):
                                    imagebutton:
                                        idle ch_icon
                                        sensitive not room.isDisabled(flags)
                                        focus_mask True
                                        action [
                                            SetVariable('prev_room', cur_room),
                                            SetVariable('cur_room', room),
                                            Call("after_return_from_room_navigation", label_name_to_call = "change_room"),
                                        ]
                                        at small_face

            # Room name
            text room.name:
                size gui.little_text_size
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
