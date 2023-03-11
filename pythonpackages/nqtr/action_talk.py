from typing import Optional, Union

from pythonpackages.nqtr.button import Button
from pythonpackages.renpy_custom_log import *
from pythonpackages.utility import *

# TODO to move in renpy
DEFAULT_LABEL_TALK = "talk"


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
        disabled: Union[bool, str] = False,
        hidden: Union[bool, str] = False,
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

    def getButtonIcon(self) -> Optional[str]:
        if (self.button_icon != None):
            return self.button_icon
        else:
            return None
