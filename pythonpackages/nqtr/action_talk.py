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
        bg: Optional[str] = None,
        # Button
        name: Optional[str] = None,
        label_name: Optional[str] = None,
        button_icon: Optional[str] = None,
        button_icon_selected: Optional[str] = None,
        picture_in_background: Optional[str] = None,
        picture_in_background_selected: Optional[str] = None,
        xalign: Optional[int] = None,
        yalign: Optional[int] = None,
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

    def isButton(self) -> bool:  # TODO: convert to a property
        """This is a button?"""
        return not isNullOrEmpty(self.button_icon)

    def isPictureInBackground(self) -> bool:  # TODO: convert to a property
        """This is a is picture in background?"""
        return not isNullOrEmpty(self.picture_in_background)

    def getTalkLabelName(self) -> None:  # TODO: convert to a property
        # if label_name == None does the default procedure
        if not isNullOrEmpty(self.label_name):
            return self.label_name
        elif not isNullOrEmpty(DEFAULT_LABEL_TALK):
            return DEFAULT_LABEL_TALK
        else:
            log_error("DEFAULT_LABEL_TALK is null or empty",
                      "nqtr.action_talk.TalkObject.getTalkLabelName()")
        return

    def getBackground(self) -> str:  # TODO: convert to a property
        """Returns the image during a conversation"""
        return self.bg

    def getButtonIcon(self) -> Optional[str]:  # TODO: convert to a property
        if (self.button_icon != None):
            return self.button_icon
        else:
            return None
