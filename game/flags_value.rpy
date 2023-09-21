# Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags
define flag_keys = [
    # Block all spend_time
    "not_can_spend_time",
    "goout",
    ""
]

# Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Flags#update_current_flags
label update_current_flags_custom:
    # Custom code
    if tm.is_weekend:
        $ set_flags("weekend", True)
        $ set_flags("not_weekend", False)
    else:
        $ set_flags("weekend", False)
        $ set_flags("not_weekend", True)
    return
