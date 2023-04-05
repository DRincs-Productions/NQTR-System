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
        bg: Optional[str] = None,  # conversation_background
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
            default_label_name=DEFAULT_LABEL_TALK,
        )

        self.bg = bg

    def getBackground(self) -> str:  # TODO: convert to a property
        """Returns the image during a conversation"""
        return self.bg
