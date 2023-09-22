# Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags
define flag_keys = [
    # Block all spend_time
    "not_can_spend_time",
    "goout",
    "weekend",
]

# Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags#update_current_flags
label update_current_flags_custom:
    # Custom code
    if tm.is_weekend:
        $ set_flags("weekend", True)
    else:
        $ set_flags("weekend", False)
    return
