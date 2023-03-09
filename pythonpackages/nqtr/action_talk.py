from pythonpackages.nqtr.button import Button
from pythonpackages.renpy_custom_log import *
from pythonpackages.utility import *

DEFAULT_LABEL_TALK = "talk"
DEFAULT_TALK_BUTTON_ICON = "/interface/action-talk.webp"


class TalkObject(Button):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system """

    def __init__(
        self,
        # only TalkObject
        bg: str = None,
        # Button
        name: str = None,
        label_name: str = None,
        button_icon: str = None,
        button_icon_selected: str = None,
        picture_in_background: str = None,
        picture_in_background_selected: str = None,
        xalign: int = None,
        yalign: int = None,
        disabled=False,  # bool | str
        hidden=False,  # bool | str
    ):
        super().__init__(
            name=name,
            label_name=label_name,
            button_icon=button_icon,
            button_icon_selected=button_icon_selected,
            picture_in_background=picture_in_background,
            picture_in_background_selected=picture_in_background_selected,
            xalign=xalign,
            yalign=yalign,
            disabled=disabled,
            hidden=hidden,
        )

        self.bg = bg

    def isButton(self) -> bool:
        """This is a button?"""
        return not isNullOrEmpty(self.button_icon)

    def isPictureInBackground(self) -> bool:
        """This is a is picture in background?"""
        return not isNullOrEmpty(self.picture_in_background)

    def getTalkLabelName(self) -> None:
        # if label_name == None does the default procedure
        if not isNullOrEmpty(self.label_name):
            return self.label_name
        elif not isNullOrEmpty(DEFAULT_LABEL_TALK):
            return DEFAULT_LABEL_TALK
        else:
            log_error("DEFAULT_LABEL_TALK is null or empty",
                      "nqtr.action_talk.TalkObject.getTalkLabelName()")
        return

    def getBackground(self) -> str:
        """Returns the image during a conversation"""
        return self.bg

    def getButtonIcon(self) -> str:
        if (self.button_icon != None):
            return self.button_icon
        else:
            return DEFAULT_TALK_BUTTON_ICON


def delTalkChoice(choice_text: str, choice_id: str, dict_choices: dict[str, list]) -> None:
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Talk-system#delete-an-action-in-default_label_talk """
    val = 0
    ch_to_del = choice_id
    for cur_choice in dict_choices[choice_id]:
        if cur_choice[0] == choice_text:
            ch_to_del = choice_id
            break
        else:
            val = val+1
    dict_choices[choice_id].pop(val)
    del val
    del ch_to_del
    return
