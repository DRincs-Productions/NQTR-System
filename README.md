# Navigation Quest Time Routine System for Ren'Py

![Last commit](https://img.shields.io/github/last-commit/DRincs-Productions/NQTR-System)
![License](https://img.shields.io/github/license/DRincs-Productions/NQTR-System)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>

**IMPORTANT**: image and some screens were taken from Big Brother for testing purposes. (Will be replaced as soon as I have time)

A complete system introducing the concepts of location, time and event, producing the framework of a not-quite-point-and-click adventure game.

This repo is a complete set of tools to create a game where you can explore and relate to characters.

Feel free to contribute, fork this and send a pull request. 😄

----

## TO DOWNLOAD THIS TEST PROJECT

```shell
# Basic command to download projects from git
git clone https://github.com/DRincs-Productions/NQTR-System
# IMPORTANT -> Will add the libraries needed to run the program
cd NQTR-System
git submodule update --init --recursive

```

----

## Documentation

**[Wiki](https://github.com/DRincs-Productions/NQTR-System/wiki)**

## Code snippets ([VSCode](https://code.visualstudio.com/))

(all begin with `DR_`)

Download the: [link](https://github.com/DRincs-Productions/NQTR-System/releases/tag/code-snippets%2Fv2.0.0)

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/67595890/179365279-0d0b6d45-0048-4a0d-8c6d-9571b9c328f4.gif)

## Install LTS Version

To install a precise version install it manually: [Releases](https://github.com/DRincs-Productions/NQTR-System/releases).

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

**AND** create a empty file `__init__.py` into `pythonpackages/` so `pythonpackages/__init__.py`.

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

## Update new version

```bash
git submodule update --init --recursive

```

## Preview

![Navigation](https://user-images.githubusercontent.com/67595890/178109985-6244ffe0-a7d6-426e-a26b-ac93ad8a300a.jpg)

![Map](https://user-images.githubusercontent.com/67595890/178110045-34cd7b96-5010-48bb-89a0-5598d5848fb0.jpg)

![Routine](https://user-images.githubusercontent.com/67595890/178110207-3b0d2932-dd08-4937-8897-47b65c70b33d.jpg)
