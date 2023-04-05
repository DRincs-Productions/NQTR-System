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
        # Deprecation: use conversation_background
        background: Optional[str] = None,
        conversation_background: Optional[str] = None,
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
        if conversation_background:
            self.conversation_background = conversation_background
        else:
            self.conversation_background = background

    @property
    @DeprecationWarning
    def background(self) -> Optional[str]:
        "Deprecation: use conversation_background"
        return self.conversation_background

    @background.setter
    @DeprecationWarning
    def background(self, value: Optional[str]):
        "Deprecation: use conversation_background"
        self.conversation_background = value

    @property
    def conversation_background(self) -> Optional[str]:
        "Image path shown during a conversation."
        return self._bg

    @conversation_background.setter
    def conversation_background(self, value: Optional[str]):
        self._bg = value
