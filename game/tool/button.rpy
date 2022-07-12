init -99 python:
    class Button(object):
        """Wiki: ... """

        def __init__(self,
                    name: str, # requirement
                    label_name: str, # requirement
                    button_icon: str = None,
                    button_icon_selected: str = None,
                    picture_in_background: str = None,
                    picture_in_background_selected: str = None,
                    xpos: int = None,
                    ypos: int = None):

            self.name = name
            self.label_name = label_name
            self.button_icon = button_icon
            self.button_icon_selected = button_icon_selected
            # Is an action that is started by clicking on an image in the room.
            self.picture_in_background = picture_in_background
            self.picture_in_background_selected = picture_in_background_selected
            self.xpos = xpos
            self.ypos = ypos
            if (self.xpos != None and self.ypos == None):
                renpy.log(
                    "Warn: xpos is set but ypos is not, so ypos set to 0")
                self.ypos = 0
            if (self.xpos == None and self.ypos != None):
                renpy.log(
                    "Warn: ypos is set but xpos is not, so xpos set to 0")
                self.xpos = 0
            if (isNullOrEmpty(self.button_icon) and isNullOrEmpty(self.picture_in_background)):
                renpy.log(
                    "Error: You have set button_icon and picture_in_background to None, this action will be ignored")

        def isButton(self):
            """This is a button?"""
            return not isNullOrEmpty(self.button_icon)

        def isPictureInBackground(self):
            """This is a is picture in background?"""
            return not isNullOrEmpty(self.picture_in_background)