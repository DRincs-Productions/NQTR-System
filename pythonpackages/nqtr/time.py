from pythonpackages.renpy_custom_log import *

START_DAY_HOUR = 0
MAX_DAY_HOUR = 24


class TimeHandler(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#time-handler """

    def __init__(
        self,
        hour_of_new_day: int = 5,
        hour: int = 8,
        weekend_day: int = 6,
        day: int = 0,
        event_duration: int = 6,
        hour_names=(),
        weekday_names=()
    ):
        self.hour_of_new_day = hour_of_new_day
        self.hour = hour
        self.day = day
        self.weekend_day = weekend_day
        self.event_duration = event_duration
        self.hour_names = hour_names
        self.weekday_names = weekday_names

        if self.hour_of_new_day < 0:
            log_warn("You have set hour_of_new_day < 0, so it will be set to 0.",
                     "nqtr.time.TimeHandler.__init__")
            self.hour_of_new_day = 0
        if self.hour < 0:
            log_warn("You have set hour < 0, so it will be set to 0.",
                     "nqtr.time.TimeHandler.__init__")
            self.hour = 0
        if self.day < 0:
            log_warn("You have set day < 0, so it will be set to 0.",
                     "nqtr.time.TimeHandler.__init__")
            self.day = 0
        if self.weekend_day < 0:
            log_warn("You have set weekend_day < 0, so it will be set to 6.",
                     "nqtr.time.TimeHandler.__init__")
            self.weekend_day = 6

    @property
    def hour_name(self) -> str:
        if self.hour >= 22:  # Night
            return self.hour_names[0][1]
        elif self.hour >= 19:  # Evening
            return self.hour_names[3][1]
        elif self.hour >= 12:  # Afternoon
            return self.hour_names[2][1]
        elif self.hour >= 5:  # Morning
            return self.hour_names[1][1]
        elif self.hour >= 0:  # Night
            return self.hour_names[0][1]
        else:  # Afternoon
            return self.hour_names[2][1]

    @property
    def image_time(self) -> str:
        """this variable is used to update images that change according to time.
        es: image = "sky-[tm.image_time]"""
        if self.hour >= 22:  # Night
            return "3"
        elif self.hour >= 19:  # Evening
            return "2"
        elif self.hour >= 12:  # Afternoon
            return "1"
        elif self.hour >= 5:  # Morning
            return "0"
        elif self.hour >= 0:  # Night
            return "3"
        else:  # Afternoon
            return "1"

    def get_day_number(self) -> int:  # TODO: convert to a property
        return self.day

    def get_hour_number(self) -> int:  # TODO: convert to a property
        return self.hour

    def get_weekday_number(self) -> int:  # TODO: convert to a property
        return self.day % 7

    def get_weekday_name(self) -> str:  # TODO: convert to a property
        return self.weekday_names[self.get_weekday_number()]

    # def get_day_of_month(self, hour=None):
    #     hour = self.get_hour(hour)
    #     day = self.get_day_number(hour) + 1
    #     for month in month_names:
    #         if day <= len(month[1]):
    #             break
    #         day -= len(month[1])
    #     return day

    # def get_month_name(self, hour=None):
    #     hour = self.get_hour(hour)
    #     return month_names[ self.get_month_number(hour) ][0]

    # def get_month_number(self, hour=None):
    #     hour = self.get_hour(hour)
    #     day = self.get_day_number(hour)
    #     # remember days start
    #     month_number = 0
    #     for month in month_names:
    #         if day < len(month[1]):
    #             break
    #         month_number += 1
    #         day -= len(month[1])
    #     return month_number

    def new_hour(self, amt: int = None) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-houre-manualy """
        # if it is too late you have to use new_day()
        if (amt == None):
            amt = self.event_duration
        if (self.hour < self.hour_of_new_day):
            return False

        self.hour += amt
        if (self.hour > MAX_DAY_HOUR):
            self.hour -= MAX_DAY_HOUR
        return True

    def new_day(self) -> None:  # TODO: convert to a property
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day-manualy """
        self.hour = self.hour_of_new_day
        self.day += 1
        return

    def now_is_between(self, end: int, start: int = 0, now=None) -> bool:
        if now is None:
            return (((self.hour >= start or start > end) and self.hour < end) or (self.hour >= start and (self.hour < end or start > end)))
        else:
            return (((now >= start or start > end) and now < end) or (now >= start and (now < end or start > end)))
