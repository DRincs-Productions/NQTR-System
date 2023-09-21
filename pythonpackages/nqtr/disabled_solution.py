from typing import Union

from pythonpackages.renpy_utility.flags import *
from pythonpackages.renpy_utility.renpy_custom_log import *
from pythonpackages.renpy_utility.utility import *


class DisabledClass(object):
    def __init__(
        self,
        disabled: Union[bool, str] = False,
    ):
        self.disabled = disabled

    @property
    def disabled(self) -> Union[bool, str]:
        """Disabled"""
        return self._disabled

    @disabled.setter
    def disabled(self, value: Union[bool, str]):
        self._disabled = value

    def is_disabled(self, flags: dict[str, bool] = {}) -> bool:
        """ "If disabled is a string: get the value of the flags system"""
        if isinstance(self.disabled, str):
            return get_flags(self.disabled, flags)
        else:
            return self.disabled
