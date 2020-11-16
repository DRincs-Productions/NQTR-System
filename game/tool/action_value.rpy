# "special" actions:
# they are not usual actions, but actions inserted and removed for a specific reason, for example for a quest.
# IMPORTANT: specify in sp_room the id of the room where the action will take place
default sp_actions = {}

# habitual actions
define df_actions = {
        "nap"       :   Action(_("Nap"), "/interface/action-sleep.webp", label = "nap", tm_start=5, tm_stop=23), 
        "sleep"     :   Action(_("Sleep"), "/interface/action-alarm.webp", label = "sleep", tm_start=23, tm_stop=5), 
    }
