init python:
    import pythonpackages.renpy_utility.flags as myFlags

init python:
    def update_flags():
        """update flags by making it with the same elements of flag_keys. in case you have to add them set them as False"""
        return myFlags.update_flags(flags, flag_keys)

    def get_flags(flag_id: str) -> bool:
        """returns the value of the flag_id in flags"""
        return myFlags.get_flags(flag_id, flags)

    def set_flags(flag_id: str, value: bool):
        return myFlags.set_flags(flag_id, value, flags)
