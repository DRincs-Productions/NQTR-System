init python:
    from pythonpackages.nqtr.action import Act

# habitual actions
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
# Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Action#add-an-action-in-dictionary
define df_actions = {
    "nap"       :   Act(name = _("Nap"),  button_icon = "action sleep", label_name = "nap", hour_start=5, hour_stop=23), 
    "sleep"     :   Act(name = _("Sleep"),  button_icon = "action alarm", label_name = "sleep", hour_start=23, hour_stop=5), 
}
