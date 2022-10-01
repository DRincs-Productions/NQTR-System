init -99 python:
    class Button(object):
        """Wiki: ... """

        def __init__(self,
                    name: str,  # requirement
                    label_name: str,  # onClick label
                    button_icon: str = None,
                    button_icon_selected: str = None,
                    picture_in_background: str = None,
                    picture_in_background_selected: str = None,
                    xalign: int = None,
                    yalign: int = None):

            self.name = name
            self.label_name = label_name
            self.button_icon = button_icon
            self.button_icon_selected = button_icon_selected
            # Is an action that is started by clicking on an image in the room.
            self.picture_in_background = picture_in_background
            self.picture_in_background_selected = picture_in_background_selected
            self.xalign = xalign
            self.yalign = yalign
            if (self.xalign != None and self.yalign == None):
                renpy.log(
                    "Warn: xalign is set but yalign is not, so yalign set to 0")
                self.yalign = 0
            if (self.xalign == None and self.yalign != None):
                renpy.log(
                    "Warn: yalign is set but xalign is not, so xalign set to 0")
                self.xalign = 0
            if (isNullOrEmpty(self.button_icon) and isNullOrEmpty(self.picture_in_background)):
                renpy.log(
                    "Error: You have set button_icon and picture_in_background to None, this action will be ignored")

        def isButton(self):
            """This is a button?"""
            return not isNullOrEmpty(self.button_icon)

        def isPictureInBackground(self):
            """This is a is picture in background?"""
            return not isNullOrEmpty(self.picture_in_background)