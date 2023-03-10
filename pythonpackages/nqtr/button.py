from pythonpackages.flags import *
from pythonpackages.renpy_custom_log import *
from pythonpackages.utility import *


class Button(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Button """

    def __init__(
        self,
        name: str,  # requirement
        label_name: str,  # onClick label
        button_icon: str = None,
        button_icon_selected: str = None,
        picture_in_background: str = None,
        picture_in_background_selected: str = None,
        xalign: int = None,
        yalign: int = None,
        disabled=False,  # bool | str
        hidden=False,  # bool | str
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

    def isButton(self) -> bool:
        """This is a button?"""
        return not isNullOrEmpty(self.button_icon)

    def isPictureInBackground(self) -> bool:
        """This is a is picture in background?"""
        return not isNullOrEmpty(self.picture_in_background)

    def isDisabled(self) -> bool:
        """"If disabled is a string: get the value of the flags system"""
        if (isinstance(self.disabled, str)):
            return getFlags(self.disabled)
        else:
            return self.disabled

    def isHidden(self) -> bool:
        """"If hidden is a string: get the value of the flags system"""
        if (isinstance(self.hidden, str)):
            return getFlags(self.hidden)
        else:
            return self.hidden

    def getButtonOrDefault(self) -> str:
        if (not isNullOrEmpty(self.button_icon)):
            return self.button_icon
        elif (not isNullOrEmpty(self.picture_in_background)):
            return self.picture_in_background
        else:
            log_error("You have set button_icon and picture_in_background to None, this button will be ignored",
                      "nqtr.button.Button.getButtonOrDefault()")
        return ""

    def getPictureInBackgroundOrDefault(self) -> str:
        if (not isNullOrEmpty(self.picture_in_background)):
            return self.picture_in_background
        elif (not isNullOrEmpty(self.button_icon)):
            return self.button_icon
        else:
            log_error("You have set button_icon and picture_in_background to None, this button will be ignored",
                      "nqtr.button.Button.getPictureInBackgroundOrDefault()")
        return ""

    def getSelectedButtonOrDefault(self) -> str:
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
