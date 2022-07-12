# dictionary editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default actions = {}

# habitual actions
# dictionary that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_actions = {
    "nap"       :   Act(name = _("Nap"),  button_icon = "/interface/action-sleep.webp", label_name = "nap", tm_start=5, tm_stop=23), 
    "sleep"     :   Act(name = _("Sleep"),  button_icon = "/interface/action-alarm.webp", label_name = "sleep", tm_start=23, tm_stop=5), 
}
