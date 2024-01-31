from typing import Optional, Union

from pythonpackages.nqtr.button import Button
from pythonpackages.renpy_utility.renpy_custom_log import *
from pythonpackages.renpy_utility.utility import *
import renpy.character as character

# TODO to move in renpy
DEFAULT_LABEL_TALK = "nqtr_talk"


class Conversation(Button):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Conversation-system"""

    def __init__(
        self,
        # only Conversation
        conversation_background: Optional[str] = None,
        characters: Optional[
            Union[list[character.ADVCharacter], character.ADVCharacter]
        ] = [],
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

        if characters:
            if isinstance(characters, character.ADVCharacter):
                characters = [characters]
        else:
            characters = []
        if len(characters) == 0:
            log_error(
                f"Conversation {self.name} has no characters. This not work.",
                filename_line="pythonpackages/nqtr/conversation.py:Conversation.__init__",
            )
        self.characters = characters
        self.conversation_background = conversation_background

    @property
    def background(self) -> Optional[str]:
        "Deprecation: use conversation_background"
        return self.conversation_background

    @background.setter
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

    @property
    def characters(self) -> list[character.ADVCharacter]:
        """List of characters involved in the conversation."""
        return self._characters

    @characters.setter
    def characters(self, value: list[character.ADVCharacter]):
        self._characters = value

    @property
    def character(self) -> Optional[character.ADVCharacter]:
        """The first character involved in the conversation."""
        if len(self.characters) > 0:
            return self.characters[0]
        else:
            return None

    @property
    def character_icons(self) -> list[str]:
        """List of character icons involved in the conversation."""
        icons: list[str] = []
        for ch in self.characters:
            # if ch have a property icon
            if "icon" in ch.who_args and isinstance(ch.who_args["icon"], str):
                icons.append(ch.who_args["icon"])
        return icons

    @property
    def character_icon(self) -> Optional[str]:
        """Returns the first icon of the characters in the commitment."""
        for ch in self.characters:
            # if ch have a property icon
            if "icon" in ch.who_args and isinstance(ch.who_args["icon"], str):
                return ch.who_args["icon"]
        return None
