default prev_room = None
default cur_room = None
default prev_location = None
default cur_location = None
default cur_map_id = None
# Variable to check the map screen: if it is True then the player is viewing the map.
default map_open = False

# list of closed rooms is checked change_room
# is composed of id = room_id and Commitment()
# expired elements are checked in after_spending_time, if you don't want an expiration: hour_stop = None
# TODO: Wiki
default closed_rooms = {}
