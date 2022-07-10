# "special" actions:
# they are not usual actions, but actions inserted and removed for a specific reason, for example for a quest.
# IMPORTANT: specify in room the id of the room where the action will take place
default sp_actions = {}

# habitual actions
define df_actions = {
    "nap"       :   Action(name = _("Nap"),  button_icon = "/interface/action-sleep.webp", label_name = "nap", tm_start=5, tm_stop=23), 
    "sleep"     :   Action(name = _("Sleep"),  button_icon = "/interface/action-alarm.webp", label_name = "sleep", tm_start=23, tm_stop=5), 
}
