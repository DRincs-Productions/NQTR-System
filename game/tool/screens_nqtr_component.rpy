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

screen action_button(act, show_picture_in_background = False):
    if not show_picture_in_background:
        if not act.isButton():
            imagebutton:
                align (act.xalign, act.yalign)
                idle act.getPictureInBackgroundOrDefault()
                hover act.getSelectedPictureInBackgroundOrDefault()
                focus_mask True
                action [
                    Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
                ]
                if renpy.variant("pc"):
                    tooltip act.name
                at middle_action_is_in_room
    elif (act.isButton() == True and not act.isHidden(flags)):
        imagebutton:
            idle act.getButtonOrDefault()
            hover act.getSelectedButtonOrDefault()
            focus_mask True
            action [
                Call("after_return_from_room_navigation", label_name_to_call = act.label_name),
            ]
            if renpy.variant("pc"):
                tooltip act.name
            at middle_action

screen action_talk_button(ch_id, talk_obj, background):
    if (not talk_obj.isHidden(flags)):
        frame:
            xysize (120, 120)
            background None

            imagebutton:
                idle talk_obj.getButtonIcon() or gui.default_talk_button_icon
                hover talk_obj.getSelectedButtonOrDefault()
                focus_mask True
                action [
                    SetVariable('talk_ch', ch_id),
                    SetVariable('talk_image', background),
                    Call("after_return_from_room_navigation", label_name_to_call = talk_obj.getTalkLabelName()),
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
                        Call("after_return_from_room_navigation", label_name_to_call = talk_obj.getTalkLabelName()),
                    ]
            if renpy.variant("pc"):
                tooltip _("Talk")
