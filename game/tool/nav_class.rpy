init -9 python:
    class Room:
        """Class of a Room"""
        def __init__(self, id, id_location, name=None, icon=None, bg=None, actions=[]):
            self.id = id
            self.id_location = id_location
            self.name = name
            self.icon = icon
            self.bg = bg
            self.actions = actions
