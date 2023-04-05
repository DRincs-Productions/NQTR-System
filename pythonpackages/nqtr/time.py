from pythonpackages.renpy_custom_log import *

MIN_DAY_HOUR = 0
MAX_DAY_HOUR = 24
DEFAULT_TIME_SPENT = 1


class TimeHandler(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#time-handler """

    def __init__(
        self,
        hour_of_new_day: int = 5,
        hour: int = 8,
        weekend_day: int = 6,
        day: int = 0,
        hour_names=(),
        weekday_names=()
    ):
        self.hour_of_new_day = hour_of_new_day
        self.hour_number = hour
        self.day_number = day
        self.weekend_day = weekend_day
        self.hour_names = hour_names
        self.weekday_names = weekday_names

        if self.hour_of_new_day < 0:
            log_warn("You have set hour_of_new_day < 0, so it will be set to 0.",
                     "nqtr.time.TimeHandler.__init__")
            self.hour_of_new_day = 0
        if self.hour_number < 0:
            log_warn("You have set hour < 0, so it will be set to 0.",
                     "nqtr.time.TimeHandler.__init__")
            self.hour_number = 0
        if self.day_number < 0:
            log_warn("You have set day < 0, so it will be set to 0.",
                     "nqtr.time.TimeHandler.__init__")
            self.day_number = 0
        if self.weekend_day < 0:
            log_warn("You have set weekend_day < 0, so it will be set to 6.",
                     "nqtr.time.TimeHandler.__init__")
            self.weekend_day = 6

    @property
    def hour_name(self) -> str:
        if self.hour_number >= 22:  # Night
            return self.hour_names[0][1]
        elif self.hour_number >= 19:  # Evening
            return self.hour_names[3][1]
        elif self.hour_number >= 12:  # Afternoon
            return self.hour_names[2][1]
        elif self.hour_number >= 5:  # Morning
            return self.hour_names[1][1]
        elif self.hour_number >= 0:  # Night
            return self.hour_names[0][1]
        else:  # Afternoon
            return self.hour_names[2][1]

    @property
    def image_time(self) -> str:
        """this variable is used to update images that change according to time.
        es: image = "sky-[tm.image_time]"""
        if self.hour_number >= 22:  # Night
            return "3"
        elif self.hour_number >= 19:  # Evening
            return "2"
        elif self.hour_number >= 12:  # Afternoon
            return "1"
        elif self.hour_number >= 5:  # Morning
            return "0"
        elif self.hour_number >= 0:  # Night
            return "3"
        else:  # Afternoon
            return "1"

    @property
    def day_number(self) -> int:
        return self._day

    @day_number.setter
    def day_number(self, value: int):
        self._day = value

    @property
    def hour_number(self) -> int:
        return self._hour

    @hour_number.setter
    def hour_number(self, value: int):
        self._hour = value
        if (self._hour > MAX_DAY_HOUR):
            self._hour = MAX_DAY_HOUR
        if (self._hour < MIN_DAY_HOUR):
            self._hour = MIN_DAY_HOUR

    @property
    def weekday_number(self) -> int:
        return self.day_number % 7

    @property
    def weekday_name(self) -> str:
        return self.weekday_names[self.weekday_number]

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

    def new_hour(self, amt: int = DEFAULT_TIME_SPENT) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-houre-manualy """
        if (self.hour_number < self.hour_of_new_day):
            return False

        self.hour_number += amt
        return True

    def new_day(self) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day-manualy """
        self.hour_number = self.hour_of_new_day
        self.day_number += 1
        return True

    def now_is_between(self, end: int, start: int = 0, now=None) -> bool:
        if now is None:
            return (((self.hour_number >= start or start > end) and self.hour_number < end) or (self.hour_number >= start and (self.hour_number < end or start > end)))
        else:
            return (((now >= start or start > end) and now < end) or (now >= start and (now < end or start > end)))
