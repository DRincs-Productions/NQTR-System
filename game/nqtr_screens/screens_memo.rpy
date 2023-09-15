# Id of the task selected in the menu
default cur_task_menu = ""
# quest level based on the task selected in the menu
default cur_quest_menu = ""

screen menu_memo():

    roll_forward True
    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"
    add "gui/overlay/game_menu.png"

    use menu_tile(_("{b}Memo{/b}"))

    # Synchronize number_stages_completed_in_quest with quests
    $ update_quests_levels()

    use close_button("menu_memo")

    frame:
        ypos 170
        xpos 80
        xsize 400
        ysize gui.lateralframescroll_ysize
        background None
        # task title list
        viewport mousewheel True draggable True id 'menu_memo_task_title_list':
            has vbox
            spacing 5
            for task_id in current_quest_stages.keys():
                button:
                    xpos gui.interface_text_size
                    xsize 390
                    background None
                    action [
                        SetVariable('cur_task_menu', task_id),
                        SetVariable('cur_quest_menu', number_stages_completed_in_quest[task_id])
                    ]
                    xpadding 0
                    ypadding 0
                    xmargin 0
                    ymargin 0
                    textbutton quests[task_id].title:
                        action [
                            SetVariable('cur_task_menu', task_id),
                            SetVariable('cur_quest_menu', number_stages_completed_in_quest[task_id]),
                        ]
                        selected cur_task_menu == task_id
        # scroll bar
        vbar value YScrollValue('menu_memo_task_title_list') style 'menu_vscroll'

    # Information on the current quest
    if cur_task_menu != '':
        $ quest_menu = quest_stages[quests[cur_task_menu].stage_ids[cur_quest_menu]]
        vbox:
            xalign 0.72
            yalign 0.6
            # Image
            if quest_menu.info_image != '' and quest_menu.info_image != None:
                add Frame(quest_menu.info_image, Borders(0,0,0,0)):
                    xsize gui.menu_memo_image_xsize
                    ysize gui.menu_memo_image_ysize
                    xalign 0.5
                    yalign 0
            elif quests[cur_task_menu].info_image != '' and quests[cur_task_menu].info_image != None:
                add Frame(quests[cur_task_menu].info_image, Borders(0,0,0,0)):
                    xsize gui.menu_memo_image_xsize
                    ysize gui.menu_memo_image_ysize
                    xalign 0.5
                    yalign 0

            text quest_menu.title:
                size gui.interface_text_size
                xalign 0.5

            frame:
                # area (0, 0, 1190, 400)
                xsize gui.menu_memo_frame_xsize
                ysize gui.menu_memo_frame_ysize
                background None

                has hbox
                viewport mousewheel True draggable True id 'vp2':
                    has vbox spacing 30
                    if cur_task_menu in quests_descriptions:
                        text quests_descriptions[cur_task_menu] size gui.normal_text_size color gui.accent_color
                    else:
                        text quests[cur_task_menu].description size gui.normal_text_size color gui.accent_color
                    if (current_quest_stages[cur_task_menu].active):
                        text quest_menu.description size gui.normal_text_size
                        text quest_menu.advice size gui.big_normal_text_size
                        for item in quest_menu.goals:
                            text item.description size gui.big_normal_text_size
                        if current_quest_stages[cur_task_menu].completed and (cur_quest_menu+1) == len(quests[cur_task_menu].stage_ids):
                            if quests[cur_task_menu].development:
                                text _("It is currently the end of this story, unfortunately you have to wait for an update to continue this story.") size gui.big_normal_text_size
                            else:
                                text _("You have completed all the quests.") size gui.big_normal_text_size
                    else:
                        text quest_menu.request_description size gui.normal_text_size color gui.accent_color
                vbar value YScrollValue('vp2') style 'menu_vscroll'

    if (cur_task_menu != '' and number_stages_completed_in_quest[cur_task_menu] > 0):
        # increases and decreases cur_quest menu
        imagebutton align (680/1920, 340/1080):
            idle '/nqtr_interface/button/next_idle.webp'
            focus_mask True
            sensitive (cur_quest_menu > 0)
            action [
                SetVariable('cur_quest_menu', cur_quest_menu - 1),
            ]
            at next_button_tran(180)
        imagebutton align (1580/1920, 340/1080):
            idle '/nqtr_interface/button/next_idle.webp'
            focus_mask True
            sensitive (cur_quest_menu < number_stages_completed_in_quest[cur_task_menu])
            action [
                SetVariable('cur_quest_menu', cur_quest_menu + 1),
            ]
            at next_button_tran(0)

    key 'K_ESCAPE' action Hide('menu_memo')
    key 'mouseup_3' action Hide('menu_memo')
