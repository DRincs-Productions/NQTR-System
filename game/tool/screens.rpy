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
    transform small_map:
        size (80, 80)
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
    transform close_zoom:
        xanchor 25
        size (75, 25)
    transform close_zoom_mobile:
        xanchor 35
        size (105, 35)

style menu_vscroll is vscrollbar:
    xsize 7
    unscrollable 'hide'

# Id of the task selected in the menu
default cur_task_menu = ""
# quest level based on the task selected in the menu
default cur_quest_menu = ""

screen room_navigation():
    modal True
    $ i = 0
    # More information by hovering the mouse
    $ (x,y) = renpy.get_mouse_pos()

    if (map_looking):
        for location in locations.values():
            # If the Map where I am is the same as the Map where the room is located
            if (location.key_map == cur_location.key_map):
                vbox:
                    align (location.yalign, location.xalign)
                    imagebutton:
                        idle location.icon
                        selected_idle location.icon + ' a'
                        selected_hover location.icon + ' a'
                        selected location == cur_location focus_mask True at small_map
                        action [Hide('wait_navigation'), SetVariable('cur_location', location), Jump('close_map')]

                    # Locations name
                    text location.name font 'DejaVuSans.ttf' size 18 drop_shadow [(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2

    else:
        hbox:
            yalign 0.99
            xalign 0.01
            spacing 2

            for room in rooms:
                $ i += 1

                # If the Locations where I am is the same as the Locations where the room is located
                if (room.id_location == cur_location.id):
                    button xysize (126, 190) action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), SetVariable('sp_bg_change_room', getBgRoomRoutine(cur_routines_location, room.id)), Jump('change_room')]:
                        has vbox xsize 126 spacing 0
                        frame xysize (126, 140) background None:
                            # Room icon
                            imagebutton:
                                align (0.5, 0.0)
                                idle room.icon
                                selected_idle room.icon + ' a'
                                selected_hover room.icon + ' a'
                                selected room == cur_room focus_mask True at middle_room
                                action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), SetVariable('sp_bg_change_room', getBgRoomRoutine(cur_routines_location, room.id)), Jump('change_room')]

                            # Check the presence of ch in that room
                            $ there_are_ch = False
                            for routine in cur_routines_location.values():
                                # If it is the selected room
                                if routine != None and room.id == routine.id_room:
                                    # I insert hbox only if they are sure that someone is there
                                    $ there_are_ch = True

                            if there_are_ch:
                                hbox ypos 73 xalign 0.5 spacing - 30:
                                    for routine in cur_routines_location.values():
                                        # If it is the selected room
                                        if room.id == routine.id_room:
                                            for ch_icon in routine.getChIcons():
                                                imagebutton idle ch_icon focus_mask True at small_face:
                                                    action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), SetVariable('sp_bg_change_room', getBgRoomRoutine(cur_routines_location, room.id)), Jump('change_room')]

                        # Room name
                        text room.name font 'DejaVuSans.ttf' size 18 drop_shadow [(2, 2)] xalign 0.5 text_align 0.5 line_leading 0 line_spacing -2
                    key str(i) action [Hide('wait_navigation'), SetVariable('prev_room', cur_room), SetVariable('cur_room', room), SetVariable('sp_bg_change_room', getBgRoomRoutine(cur_routines_location, room.id)), Jump('change_room')]

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

                # Adds a talk for each ch (NPC) and at the talk interval adds the icon for each secondary ch
                # TODO: there is no possibility of group talk
                for routine in cur_routines_location.values():
                    if (routine != None and room.id == routine.id_room and room == cur_room):
                        # Insert in talk for every ch, main in that room
                        for ch in routine.chs.keys():
                            frame xysize (120, 120) background None:
                                imagebutton:
                                    idle '/interface/action-talk.webp'
                                    focus_mask True
                                    action [Hide('wait_navigation'), SetVariable('talk_ch', ch), SetVariable('talk_image', routine.getTalkImage(ch)), SetVariable('talk_end_image', routine.getAfterTalkImage(ch)), Function(routine.talk, ch)]
                                    at middle_action
                                # inserts the icon of the character who is currently in that room
                                # TODO: for now insert only the icon of the main ch, I have to insert also the icon of the other secondary ch
                                imagebutton:
                                    idle ch_icons.get(ch)
                                    focus_mask True
                                    at small_face
                                    action [Hide('wait_navigation'), SetVariable('talk_ch', ch), SetVariable('talk_image', routine.getTalkImage(ch)), SetVariable('talk_end_image', routine.getAfterTalkImage(ch)), Function(routine.talk, ch)]
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
    hbox:
        align (0.5, 0.01)
        vbox:
            align (0.5, 0.01)
            text "[tm.hour]:00" xalign (0.5) font 'DejaVuSans.ttf' size 60 drop_shadow [(2, 2)]
            text tm.get_weekday_name() xalign (0.5) font 'DejaVuSans.ttf' size 24 drop_shadow [(2, 2)] line_leading -16

        if (map_looking):
            # Fixed button to wait
            imagebutton:
                xysize (300, 300)
                idle '/interface/action-wait.webp'
                focus_mask True
                action [Hide('wait_navigation'), Jump('wait_onehour')]
                if renpy.variant("pc"):
                    tooltip _("Wait")
                at middle_action

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
            if len(current_quest_stages) > 0 :
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
            action [Hide('wait_navigation'), Jump('open_map')]
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

screen menu_memo():
    style_prefix "game_menu"
    # Synchronize quests_levels with quests
    $ updateQuestsLevels()

    add '/gui/overlay/game_menu.png'

    # button for closure
    imagebutton:
        pos (1740, 100)
        idle '/interface/button/close_idle.webp'
        hover '/interface/button/close_hover.webp'
        action [Hide('menu_memo')]
        if renpy.variant("pc"):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_mobile

    hbox pos (150, 150) spacing 30:
        frame ypos 25 xsize 400 ysize 850 background None:
            has hbox
            # task title list
            viewport mousewheel 'change' draggable True id 'vp1':
                has vbox spacing 5
                for id_task in current_quest_stages.keys():
                    button:
                        xsize 390
                        background None
                        action [SetVariable('cur_task_menu', id_task), SetVariable('cur_quest_menu', quests_levels[id_task])]
                        xpadding 0 ypadding 0 xmargin 0 ymargin 0
                        textbutton quests[id_task].title:
                            action [SetVariable('cur_task_menu', id_task), SetVariable('cur_quest_menu', quests_levels[id_task])]
                            selected cur_task_menu == id_task
            # scroll bar
            vbar value YScrollValue('vp1') style 'menu_vscroll'

        # Information on the current quest
        if cur_task_menu != '':
            $ quest_menu = quest_stages[quests[cur_task_menu].stages_id[cur_quest_menu]]
            frame area (0, 30, 1190, 850) background None:
                has vbox spacing 20
                # Image
                if quest_menu.bg != '' and quest_menu.bg != None:
                    add Frame(quest_menu.bg, Borders(0,0,0,0)):
                        xsize 800
                        ysize 400
                        pos (195,0)
                elif quests[cur_task_menu].bg != '' and quests[cur_task_menu].bg != None:
                    add Frame(quests[cur_task_menu].bg, Borders(0,0,0,0)):
                        xsize 800
                        ysize 400
                        pos (195,0)
                frame xsize 1180 xalign 0.5 background None:
                    text quest_menu.title size 30 font 'DejaVuSans.ttf' xalign 0.5
                frame area (0, 0, 1190, 400) background None:
                    has hbox
                    viewport mousewheel 'change' draggable True id 'vp2':
                        has vbox spacing 30
                        if cur_task_menu in quests_descriptions:
                            text quests_descriptions[cur_task_menu] size 24 color gui.accent_color
                        else:
                            text quests[cur_task_menu].description size 24 color gui.accent_color
                        if (current_quest_stages[cur_task_menu].active):
                            text quest_menu.description size 24
                            text quest_menu.advice size 28
                            for item in quest_menu.goals:
                                text item.description size 28
                            if current_quest_stages[cur_task_menu].completed and (cur_quest_menu+1) == len(quests[cur_task_menu].stages_id):
                                if quests[cur_task_menu].development:
                                    text _("It is currently the end of this story, unfortunately you have to wait for an update to continue this story.") size 28
                                else:
                                    text _("You have completed all the quests.") size 28
                        else:
                            text quest_menu.description_request size 24 color gui.accent_color
                    vbar value YScrollValue('vp2') style 'menu_vscroll'
    if (cur_task_menu != '' and quests_levels[cur_task_menu] > 0):
        # increases and decreases cur_quest menu
        imagebutton pos (690, 360):
            idle '/interface/button/prev_idle.webp'
            hover '/interface/button/prev_hover.webp'
            insensitive '/interface/button/prev_insensitive.webp'
            focus_mask True
            sensitive (cur_quest_menu > 0)
            action [SetVariable('cur_quest_menu', cur_quest_menu-1)]
        imagebutton pos (1570, 360):
            idle '/interface/button/next_idle.webp'
            hover '/interface/button/next_hover.webp'
            insensitive '/interface/button/next_insensitive.webp'
            focus_mask True
            sensitive (cur_quest_menu < quests_levels[cur_task_menu])
            action [SetVariable('cur_quest_menu', cur_quest_menu+1)]
