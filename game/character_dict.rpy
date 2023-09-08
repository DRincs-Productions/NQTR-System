init -1 python:
    from pythonpackages.renpy_utility.character_custom import DRCharacter

init 9:
    # Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Character-Disct
    define character_dict = {
        "alice"     :   DRCharacter(character = a, icon = "icon/Alice.webp"),
        "ann"       :   DRCharacter(character = an, icon = "icon/Ann.webp"),
    }
