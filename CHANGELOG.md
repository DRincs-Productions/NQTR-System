# LTS Version

## Install

You can install this library manually: download the zip and extract it in your project folder.
But I recommend you to use git submodule:

```bash
# renpy-utility-lib
git submodule add -b python-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'pythonpackages/renpy_utility'
git submodule add -b renpy-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'game/renpy_utility_tool'
# renpy-utility-lib
git submodule add -b main -- https://github.com/DRincs-Productions/renpy-screens-style 'game/screens_style'
# NQTR-System
git submodule add -b python-lib -- https://github.com/DRincs-Productions/NQTR-System 'pythonpackages/nqtr'
git submodule add -b renpy-lib -- https://github.com/DRincs-Productions/NQTR-System 'game/nqtr_tool'
git submodule add -b screens -- https://github.com/DRincs-Productions/NQTR-System 'game/nqtr_screens'
git submodule add -b interface-images -- https://github.com/DRincs-Productions/NQTR-System 'game/nqtr_interface'

```

**AND** create a empty file `__init__.py` into pythonpackages `pythonpackages/` so `pythonpackages/__init__.py`.

add `after_load` into `core.rpy` for update values after game update:

```renpy
label after_load:
    # ...

    # renpy-utility-lib
    call update_current_flags(update_dictionary = True)

    # nqtr
    python:
        # timeHandler update: if you update TimeHandler settings into a new version, you can use this function to update the old save files.
        updateTimeHandler(tm)
        # clear the expired actions and routine
        from pythonpackages.nqtr.action import clear_expired_actions
        from pythonpackages.nqtr.routine import clear_expired_routine
        clear_expired_actions(actions, tm.day)
        clear_expired_routine(routine, tm)
        # recheck the character's events and commitments in current location
        from pythonpackages.nqtr.routine import characters_events_in_current_location
        from pythonpackages.nqtr.routine import characters_commitment_in_current_location
        cur_events_location = characters_events_in_current_location(cur_location.id, routine, tm, flags)
        commitments_in_cur_location = characters_commitment_in_current_location(cur_location.id, routine | df_routine, tm, flags)
        # update the quest levels, if ypu add a new stage in the quest, you can use this function to start the new stage
        update_quests_levels()
    return
```

## Migrations

Use search and replace of vscode with regex functionality enabled

![image](https://user-images.githubusercontent.com/67595890/224504331-1f546922-5673-4fa9-8cc7-e3fc4e671305.png)

### Routine Migration

For exemple:

the old routine:

```renpy
init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.action_talk import TalkObject

define df_routine = {
    # ...
    "alice_read" : Commitment(
        ch_talkobj_dict={
            "alice" : TalkObject(
                name="talk_alice_read",

                conversation_background ="bg alice terrace talk"
            ),
        },
        hour_start=10, hour_stop=20,
        location_id="house", room_id="terrace",
        background ="bg alice terrace",
    ),
}
```

the new routine:

```renpy
init python:
    from pythonpackages.nqtr.routine import Commitment
    from pythonpackages.nqtr.action_talk import Conversation

define df_routine = {
    # ...
    "alice_read" : Commitment(
        conversations = [
            Conversation(
                name="talk_alice_read",
                characters=a,
                conversation_background ="bg alice terrace talk"
            ),
        ],
        hour_start=10, hour_stop=20,
        location_id="house", room_id="terrace",
        background ="bg alice terrace",
    ),
}
```

### Conversation Migration

For exemple:

to add conversation:

```renpy
python:
    add_talk_choice(choice_id = "alice", choice_text = _("About the Ann"), label_name = "stage_talkalice_aboutann", dict_choices = talkch_choices)
```

now:

```renpy
python:
    add_conversation_choice(choice_character = a, choice_text = _("About the Ann"), label_name = "stage_talkalice_aboutann")
```

to remove conversation:

```renpy
python:
    del_talk_choice(choice_id = "alice", choice_text = _("About the Ann"), dict_choices = talkch_choices)
```

now:

```renpy
python:
    del_conversation_choice(choice_character = a, choice_text = _("About the Ann"))
```

### getTalkLabelName

* `getTalkLabelName\(\)`
* `label_name`

### getButtonIcon

* `getButtonIcon\(\)`
* `button_icon`

### get_hour_name

* `get_hour_name\(\)`
* `timeslot_name`

### get_day_number

* `get_day_number\(\)`
* `day`

### get_hour_number

* `get_hour_number\(\)`
* `hour`

### get_weekday_number

* `get_weekday_number\(\)`
* `weekday_number`

### get_weekday_name

* `get_weekday_name\(\)`
* `weekday_name`

### isEvent

* `isEvent\(\)`
* `is_event`

### getBackground

* `getBackground\(\)`
* `background`

### bg

* `bg =(.*)`
* `background =$1`

### bg

* `bg=(.*)`
* `background =$1`

### isButton

* `isButton\(\)`
* `is_button`

### isPictureInBackground

* `isPictureInBackground\(\)`
* `is_picture_in_background`

### getButtonOrDefault

* `getButtonOrDefault\(\)`
* `button_icon`

### getPictureInBackgroundOrDefault

* `getPictureInBackgroundOrDefault\(\)`
* `picture_in_background`

### getSelectedButtonOrDefault

* `getSelectedButtonOrDefault\(\)`
* `button_icon_selected`

### getSelectedPictureInBackgroundOrDefault

* `getSelectedPictureInBackgroundOrDefault\(\)`
* `picture_in_background_selected`

### image_time

* `image_time`
* `timeslot_number`

### hour_names

* `hour_names`
* `timeslot_names`

### tm_start

* `tm_start`
* `hour_start`

### tm_stop

* `tm_stop`
* `hour_stop`

### stages_id

* `stages_id`
* `stage_ids`

### number_stages_completed_in_quest_requests

* `number_stages_completed_in_quest_requests`
* `required_number_completed_stages`

### weekend_day

* `weekend_day`
* `weekday_weekend_begins`

### updateFlags

* `updateFlags\((.*)\)`
* `update_flags($1)`

### getFlags

* `getFlags\((.*)\)`
* `get_flags($1)`

### setFlags

* `setFlags\((.*)\)`
* `set_flags($1)`

### notifyEx

* `notifyEx\((.*)\)`
* `notify_add($1)`

### notifyExPreventsLoops

* `notifyExPreventsLoops\((.*)\)`
* `notify_prevents_loops($1)`

### notifyExClean

* `notifyExClean\((.*)\)`
* `notify_remove($1)`

### clearExpiredActions

* `clearExpiredActions\((.*)\)`
* `clear_expired_actions($1)`

### isDisabled

* `isDisabled\((.*)\)`
* `is_disabled($1)`

### isHidden

* `isHidden\((.*)\)`
* `is_hidden($1)`

### isClosedRoom

* `isClosedRoom\((.*)\)`
* `is_closed_room($1)`

### getRoomById

* `getRoomById\((.*)\)`
* `get_room_by_id($1)`

### getLocationById

* `getLocationById\((.*)\)`
* `get_location_by_id($1)`

### addInCurrentQuestStages

* `addInCurrentQuestStages\((.*)\)`
* `add_in_current_stages($1)`

### addInCurrentTaskStages

* `addInCurrentTaskStages\((.*)\)`
* `add_in_current_stages($1)`

### respectAllRequests

* `respectAllRequests\((.*)\)`
* `all_requests_are_met($1)`

### isCompleted

* `isCompleted\((.*)\)`
* `is_completed($1)`

### setDayNumberRequiredToStart

* `setDayNumberRequiredToStart\((.*)\)`
* `add_required_days_to_start($1)`

### currentQuestId

* `currentQuestId\((.*)\)`
* `quest_id($1)`

### completeStagesNumber

* `completeStagesNumber\((.*)\)`
* `completed_stages_number($1)`

### getPercentageCompletion

* `getPercentageCompletion\((.*)\)`
* `percentage_completion($1)`

### nextStage

* `nextStage\((.*)\)`
* `next_stage($1)`

### afterNextStage

* `afterNextStage\((.*)\)`
* `after_next_stage($1)`

### getChIcons

* `getChIcons\((.*)\)`
* `character_icons($1)`

### getTalkBackground

* `getTalkBackground\((.*)\)`
* `conversation_background($1)`

### clearExpiredRoutine

* `clearExpiredRoutine\((.*)\)`
* `clear_expired_routine($1)`

### getChsInThisLocation

* `getChsInThisLocation\((.*)\)`
* `characters_commitment_in_current_location($1)`

### getEventsInThisLocation

* `getEventsInThisLocation\((.*)\)`
* `characters_events_in_current_location($1)`

### getChLocation

* `getChLocation\((.*)\)`
* `commitment_by_character($1)`

### getBgRoomRoutine

* `getBgRoomRoutine\((.*)\)`
* `commitment_background($1)`

### updateQuestsLevels

* `updateQuestsLevels\((.*)\)`
* `update_quests_levels($1)`

### checkInactiveStage

* `checkInactiveStage\((.*)\)`
* `check_inactive_stage($1)`

### checkIfTheQuestExist

* `checkIfTheQuestExist\((.*)\)`
* `is_quest_existing($1)`

### checkIfTheQuestIsInNumberStages

* `checkIfTheQuestIsInNumberStages\((.*)\)`
* `is_quest_in_number_stages($1)`

### checkIfTheQuestIsCurrentTaskStages

* `checkIfTheQuestIsCurrentTaskStages\((.*)\)`
* `is_quest_in_current_task_stages($1)`

### checkIfTheQuestIsCurrentQuestStages

* `checkIfTheQuestIsCurrentQuestStages\((.*)\)`
* `is_quest_in_current_quest_stages($1)`

### quest_getPercentageCompletion

* `quest_getPercentageCompletion\((.*)\)`
* `quest_percentage_completion($1)`

### quest_setDayNumberRequiredToStart

* `quest_setDayNumberRequiredToStart\((.*)\)`
* `quest_add_required_days_to_start($1)`

### quest_nextStageOnlyIsCompleted

* `quest_nextStageOnlyIsCompleted\((.*)\)`
* `quest_next_stage_only_is_completed($1)`

### quest_nextStage

* `quest_nextStage\((.*)\)`
* `quest_next_stage($1)`

### quest_isStarted

* `quest_isStarted\((.*)\)`
* `quest_is_started($1)`

### quest_isCompleted

* `quest_isCompleted\((.*)\)`
* `quest_is_completed($1)`

### quest_currentQuestId

* `quest_currentQuestId\((.*)\)`
* `quest_current_quest_id($1)`

### quest_completeStagesNumber

* `quest_completeStagesNumber\((.*)\)`
* `quest_complete_stages_number($1)`

### addTalkChoice

* `addTalkChoice\((.*)\)`
* `add_conversation_choice($1)`

### delTalkChoice

* `delTalkChoice\((.*)\)`
* `del_conversation_choice($1)`

# v1.0.3

```shell
git checkout -b nqtr-tool
git checkout nqtr-tool
git config pull.rebase false
git pull https://github.com/DRincs-Productions/NQTR-System.git v1.0.3 --allow-unrelated-histories

```

Now NQTR is a python library, and renpy interacts with it through easy-to-use functions.

What it means:

Pros:

* Performance
* I can now develop directly with python. this makes my life easier since I can use the tools to develop in python
* Can create tests
* From now on future versions will have less complex migration: since now I aim to modify as little as possible renpy functions , but only the library.

Cons:

* Sharing variables with renpy and the library is slightly more difficult because it relies on pointers. (As long as I only share dictionaries, I won't have any big problems).

## Migrations

Use search and replace of vscode with regex functionality enabled

![image](https://user-images.githubusercontent.com/67595890/224504331-1f546922-5673-4fa9-8cc7-e3fc4e671305.png)

### quest_start

* `quests\["(.*)"\].start\(\)`
* `quest_start(id = "$1")`

### quest_nextStage

* `quests\["(.*)"\].nextStage\(\)`
* `quest_next_stage(id = "$1")`

### quest_nextStageOnlyIsCompleted

* `quests\["(.*)"\].nextStageOnlyIsCompleted\(\)`
* `quest_next_stage_only_is_completed(id = "$1")`

### quest_setDayNumberRequiredToStart

* `quests\["(.*)"\].SetDayNumberRequiredToStart\((.*)\)`
* `quest_add_required_days_to_start(id = "$1",$2)`

### new_day

* `tm.new_day\((.*))\`
* `new_day($1)`

### new_hour

* `tm.new_hour((.*))`
* `new_hour($1)`

### setFlags

* `flags\["(.*)"\] =(.*)`
* `setFlags("$1",$2)`

## What's Changed

* 55 convert pos to align by @DonRP in <https://github.com/DRincs-Productions/NQTR-System/pull/56>
* 57 convert all class in library py by @DonRP in <https://github.com/DRincs-Productions/NQTR-System/pull/58>

**Full Changelog**: <https://github.com/DRincs-Productions/NQTR-System/compare/v1.0.2...v1.0.3>

# v1.0.2

```shell
git checkout -b NQTR-toolkit
git checkout NQTR-toolkit
git config pull.rebase false
git pull https://github.com/DRincs-Productions/NQTR-toolkit.git v1.0.2 --allow-unrelated-histories

```

## What's Changed

* fix and improve by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/53>
* 20 add notifications and improve log by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/54>
![image](https://user-images.githubusercontent.com/67595890/198825289-292df3da-8143-4fbf-a686-24e42c744d8c.png)
![image](https://user-images.githubusercontent.com/67595890/198825291-1cf9be09-a074-49dd-9c40-8741f93dbeda.png)

**Full Changelog**: <https://github.com/DRincs-Productions/NQTR-toolkit/compare/v1.0.1...v1.0.2>

# v1.0.1

## What's Changed

* Create LICENSE by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/1>
* Ren'Py 8.0.0 by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/8>
* 9 typify python by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/10>
* 14 code snippets by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/27>
* 11 improving the quest system by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/33>
* 12 pass by object reference by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/34>
* 16 after closing a label it should not be mandatory to close with call screen room navigation by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/37>
* Update time_label.rpy by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/38>
* fix by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/41>
* align cash label by @01010100010100100100100101000111 in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/44>
* Fixes for #42 and #43 by @01010100010100100100100101000111 in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/45>
* clean by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/49>
* 15 create a button class to be extended by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/50>  (**IMPORTANT**: Some property names have been changed: So it gives errors when inserted in an old version. But it does not create any problems in saves.   )
* 4 map navigation possibility to use multiple maps by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/51>

## New Contributors

* @DonRP made their first contribution in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/1>
* @01010100010100100100100101000111 made their first contribution in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/44>

**Full Changelog**: <https://github.com/DRincs-Productions/NQTR-toolkit/commits/v1.0.1>

# v1.0.0

```shell
git checkout -b NQTR-toolkit
git checkout NQTR-toolkit
git pull https://github.com/DRincs-Productions/NQTR-toolkit.git v1.0.0 --allow-unrelated-histories

```

## What's Changed

* Create LICENSE by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/1>
* Ren'Py 8.0.0 by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/8>
* 9 typify python by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/10>
* 14 code snippets by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/27>
* 11 improving the quest system by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/33>
* 12 pass by object reference by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/34>
* 16 after closing a label it should not be mandatory to close with call screen room navigation by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/37>
* Update time_label.rpy by @DonRP in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/38>

## New Contributors

* @DonRP made their first contribution in <https://github.com/DRincs-Productions/NQTR-toolkit/pull/1>

**Full Changelog**: <https://github.com/DRincs-Productions/NQTR-toolkit/commits/v1.0.0>
