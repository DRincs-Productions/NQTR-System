# Navigation Quest Time Routine System for Ren'py

![Last commit](https://img.shields.io/github/last-commit/DRincs-Productions/NQTR-System)
![License](https://img.shields.io/github/license/DRincs-Productions/NQTR-System)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>

**IMPORTANT**: image and some screens were taken from Big Brother for testing purposes. (Will be replaced as soon as I have time)

A complete system introducing the concepts of location, time and event, producing the framework of a not-quite-point-and-click adventure game.

This repo is a complete set of tools to create a game where you can explore and relate to characters.

In order to simplify the update work and avoid errors in saving I created functions that check the correct state of variables by inserting them in [after_load](game/tool/core.rpy#L1) (e.g. after a change to a quest that causes a stage to be blocked, the quest should restart) and an abundant use of define.

Feel free to contribute, fork this and send a pull request. 😄

## Documentation

**[Wiki](https://github.com/DRincs-Productions/NQTR-System/wiki)**

## Code snippets ([VSCode](https://code.visualstudio.com/))

(all begin with `DR_`)

Download the: [link](https://github.com/DRincs-Productions/NQTR-System/releases/tag/code-snippets%2Fv2.0.0)

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/67595890/179365279-0d0b6d45-0048-4a0d-8c6d-9571b9c328f4.gif)

## Install LTS Version
You can install this library manually: download the zip and extract it in your project folder.
But I recommend you to use git submodule:
```bash
# renpy-utility-lib
git submodule add -b python-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'pythonpackages/renpy_utility'
git submodule add -b renpy-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'game/renpy_utility_tool'
# renpy-utility-lib
git submodule add -b 1080p -- https://github.com/DRincs-Productions/renpy-screens-style 'game/screens_style'
# NQTR-System
git submodule add -b python-lib -- https://github.com/DRincs-Productions/NQTR-System 'pythonpackages/nqtr'
git submodule add -b renpy-lib -- https://github.com/DRincs-Productions/NQTR-System 'game/nqtr_tool'
git submodule add -b screens -- https://github.com/DRincs-Productions/NQTR-System 'game/nqtr_screens'
git submodule add -b interface-images -- https://github.com/DRincs-Productions/NQTR-System 'game/nqtr_interface'

```

**AND** create a empty file `__init__.py` into pythonpackages `pythonpackages/` so `pythonpackages/__init__.py`.

## Update new version
```bash
git submodule update --init --recursive
```

## Preview

![Navigation](https://user-images.githubusercontent.com/67595890/178109985-6244ffe0-a7d6-426e-a26b-ac93ad8a300a.jpg)

![Map](https://user-images.githubusercontent.com/67595890/178110045-34cd7b96-5010-48bb-89a0-5598d5848fb0.jpg)

![Routine](https://user-images.githubusercontent.com/67595890/178110207-3b0d2932-dd08-4937-8897-47b65c70b33d.jpg)
