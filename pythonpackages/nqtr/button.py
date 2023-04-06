from typing import Optional, Union

from pythonpackages.flags import *
from pythonpackages.renpy_custom_log import *
from pythonpackages.utility import *


class Button(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Button """

    def __init__(
        self,
        name: str,  # requirement
        label_name: str,  # onClick label
        button_icon: Optional[str] = None,
        button_icon_selected: Optional[str] = None,
        picture_in_background: Optional[str] = None,
        picture_in_background_selected: Optional[str] = None,
        xalign: Optional[int] = None,
        yalign: Optional[int] = None,
        disabled: Union[bool, str] = False,
        hidden: Union[bool, str] = False,
        default_label_name: Optional[str] = None,
    ):

        self.name = name
        self.label_name = label_name
        self.button_icon = button_icon
        self.button_icon_selected = button_icon_selected
        # Is an action that is started by clicking on an image in the room.
        self.picture_in_background = picture_in_background
        self.picture_in_background_selected = picture_in_background_selected
        self.xalign = xalign
        self.yalign = yalign
        self.disabled = disabled
        self.hidden = hidden
        self.default_label_name = default_label_name
        if (self.xalign != None and self.yalign == None):
            log_warn("xalign is set but yalign is not, so yalign set to 0",
                     "nqtr.button.Button.__init__")
            self.yalign = 0
        if (self.xalign == None and self.yalign != None):
            log_warn("yalign is set but xalign is not, so xalign set to 0",
                     "nqtr.button.Button.__init__")
            self.xalign = 0
        if (isNullOrEmpty(self.button_icon) and isNullOrEmpty(self.picture_in_background)):
            log_info("You have set button_icon and picture_in_background to None, this action will be ignored",
                     "nqtr.button.Button.__init__")

    @property
    def label_name(self) -> Optional[str]:
        """onClick label name"""
        if not isNullOrEmpty(self._label_name):
            return self._label_name
        elif not isNullOrEmpty(self.default_label_name):
            return self.default_label_name
        else:
            log_warn("label_name is null or empty",
                     "nqtr.button.Button.label_name")
        return

    @label_name.setter
    def label_name(self, value: Optional[str]):
        self._label_name = value

    @property
    def is_button(self) -> bool:
        """This is a button?"""
        return not isNullOrEmpty(self.button_icon)

    @property
    def is_picture_in_background(self) -> bool:
        """This is a is picture in background?"""
        return not isNullOrEmpty(self._picture_in_background)

    def isPictureInBackground(self) -> bool:  # TODO: convert to a property
        """This is a is picture in background?"""
        return not isNullOrEmpty(self.picture_in_background)

    def isDisabled(self, flags: dict[str, bool] = {}) -> bool:
        """"If disabled is a string: get the value of the flags system"""
        if (isinstance(self.disabled, str)):
            return getFlags(self.disabled, flags)
        else:
            return self.disabled

    def isHidden(self, flags: dict[str, bool] = {}) -> bool:
        """"If hidden is a string: get the value of the flags system"""
        if (isinstance(self.hidden, str)):
            return getFlags(self.hidden, flags)
        else:
            return self.hidden

    @property
    def button_icon(self) -> Optional[str]:
        """Button icon"""
        if (not isNullOrEmpty(self._button_icon)):
            return self._button_icon
        else:
            log_info("You have set button_icon and picture_in_background to None, this button will be ignored",
                     "nqtr.button.Button.button_icon")
        return None

    def getButtonOrDefault(self) -> str:  # TODO: to remove
        if (not isNullOrEmpty(self.button_icon)):
            return self.button_icon
        elif (not isNullOrEmpty(self.picture_in_background)):
            return self.picture_in_background
        else:
            log_error("You have set button_icon and picture_in_background to None, this button will be ignored",
                      "nqtr.button.Button.getButtonOrDefault()")
        return ""

    @property
    def picture_in_background(self) -> Optional[str]:
        """Picture in background"""
        if (not isNullOrEmpty(self._picture_in_background)):
            return self._picture_in_background
        else:
            log_info("You have set picture_in_background and button_icon to None, this button will be ignored",
                     "nqtr.button.Button.picture_in_background")
        return None

    # TODO: to remove
    def getPictureInBackgroundOrDefault(self) -> str:
        if (not isNullOrEmpty(self.picture_in_background)):
            return self.picture_in_background
        elif (not isNullOrEmpty(self.button_icon)):
            return self.button_icon
        else:
            log_error("You have set button_icon and picture_in_background to None, this button will be ignored",
                      "nqtr.button.Button.getPictureInBackgroundOrDefault()")
        return ""

    @property
    def selected_button_icon(self) -> Optional[str]:
        """Selected button icon"""
        if (not isNullOrEmpty(self.button_icon_selected)):
            return self.button_icon_selected
        elif (not isNullOrEmpty(self.button_icon)):
            return self.button_icon
        else:
            log_info("You have set button_icon_selected and button_icon to None, this button will be ignored",
                     "nqtr.button.Button.selected_button_icon")
        return None

    def getSelectedButtonOrDefault(self) -> str:  # TODO: convert to a property
        if (not isNullOrEmpty(self.button_icon_selected)):
            return self.button_icon_selected
        elif (not isNullOrEmpty(self.button_icon)):
            return self.button_icon
        elif (not isNullOrEmpty(self.picture_in_background_selected)):
            return self.picture_in_background_selected
        elif (not isNullOrEmpty(self.picture_in_background)):
            return self.picture_in_background
        else:
            log_info("You have set button_icon_selected and picture_in_background_selected and button_icon and picture_in_background to None, this button will be ignored",
                     "nqtr.button.Button.getSelectedButtonOrDefault()")
        return ""

    @property
    def selected_picture_in_background(self) -> Optional[str]:
        """Selected picture in background"""
        if (not isNullOrEmpty(self.picture_in_background_selected)):
            return self.picture_in_background_selected
        elif (not isNullOrEmpty(self.picture_in_background)):
            return self.picture_in_background
        else:
            log_info("You have set picture_in_background_selected and picture_in_background to None, this button will be ignored",
                     "nqtr.button.Button.selected_picture_in_background")
        return None

    # TODO: convert to a property
    def getSelectedPictureInBackgroundOrDefault(self) -> str:
        if (not isNullOrEmpty(self.picture_in_background_selected)):
            return self.picture_in_background_selected
        elif (not isNullOrEmpty(self.picture_in_background)):
            return self.picture_in_background
        elif (not isNullOrEmpty(self.button_icon_selected)):
            return self.button_icon_selected
        elif (not isNullOrEmpty(self.button_icon)):
            return self.button_icon
        else:
            log_error("You have set picture_in_background_selected and button_icon_selected and button_icon and picture_in_background to None, this button will be ignored",
                      "nqtr.button.Button.getSelectedPictureInBackgroundOrDefault()")
        return ""
