init -9 python:
    class Room:
        """Class of a Room"""
        def __init__(self,
            id,
            id_location,
            name=None,
            icon=None,
            bg=None,
            actions=[]):

            self.id = id
            self.id_location = id_location
            self.name = name
            self.icon = icon
            self.bg = bg
            self.actions = actions

    class Location:
        """Class of a Location"""
        def __init__(self,
            id,
            id_map,
            id_externalroom,
            name=None,
            icon=None,
            xalign=0,
            yalign=0,
            active=True):

            self.id = id
            self.id_map = id_map
            self.name = name
            self.id_externalroom = id_externalroom
            self.icon = icon
            self.xalign = xalign
            self.yalign = yalign
