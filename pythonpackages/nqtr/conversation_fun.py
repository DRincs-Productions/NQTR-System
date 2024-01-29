from pythonpackages.nqtr.conversation import Conversation
from pythonpackages.nqtr.navigation import Room
from pythonpackages.nqtr.routine import Commitment
from pythonpackages.renpy_utility.renpy_custom_log import *
from pythonpackages.renpy_utility.utility import *
import renpy.character as character


def current_button_conversations(
    commitments_in_cur_location: dict[character.ADVCharacter, Commitment],
    room: Room,
    cur_room: Room,
) -> list[tuple[Conversation, Commitment]]:
    """Return a list of conversation buttons for the current room and available for the current time"""
    conversations: list[tuple[Conversation, Commitment]] = []
    for comm in commitments_in_cur_location.values():
        if cur_room and comm and room.id == comm.room_id and room.id == cur_room.id:
            # Insert in talk for every ch, main in that room
            for conversation in comm.conversations:
                if conversation:
                    conversations.append((conversation, comm))
    return conversations


def current_picture_in_background_conversations(
    commitments_in_cur_location: dict[character.ADVCharacter, Commitment],
    room: Room,
    cur_room: Room,
) -> list[tuple[Conversation, Commitment]]:
    """Return a list of conversation picture in background for the current room and available for the current time"""
    conversations: list[tuple[Conversation, Commitment]] = []
    for comm in commitments_in_cur_location.values():
        if cur_room and comm and room.id == comm.room_id and room.id == cur_room.id:
            # Insert in talk for every ch, main in that room
            for conversation in comm.conversations:
                if conversation and conversation.is_picture_in_background:
                    conversations.append((conversation, comm))
    return conversations
