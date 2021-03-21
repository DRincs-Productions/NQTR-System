init -9 python:
    class Room:
        """Class of a Room"""
        def __init__(self,
            id,
            id_location,
            name=None,
            icon=None,
            bg=None,
           id_actions=[]):

            self.id = id
            self.id_location = id_location
            self.name = name
            self.icon = icon
            self.bg = bg
            self.id_actions = id_actions

    class Location:
        """Class of a Location"""
        def __init__(self,
            id,
            key_map,
            id_externalroom,
            name=None,
            icon=None,
            xalign=0,
            yalign=0):

            self.id = id
            self.key_map = key_map
            self.name = name
            self.id_externalroom = id_externalroom
            self.icon = icon
            self.xalign = xalign
            self.yalign = yalign
