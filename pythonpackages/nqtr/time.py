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
        self.hour = hour
        self.day = day
        self.weekend_day = weekend_day
        self.hour_names = hour_names
        self.weekday_names = weekday_names

        if self.hour_of_new_day < 0:
            log_warn("You have set hour_of_new_day < 0, so it will be set to 0.",
                     "nqtr.time.TimeHandler.__init__")
            self.hour_of_new_day = 0
        if self.weekend_day < 0:
            log_warn("You have set weekend_day < 0, so it will be set to 6.",
                     "nqtr.time.TimeHandler.__init__")
            self.weekend_day = 6

    @property
    def day(self) -> int:
        """current day number"""
        return self._day

    @day.setter
    def day(self, value: int):
        self._day = value
        if (self._day < 0):
            self._day = 0
            log_warn("You have set day < 0, so it will be set to 0.",
                     "nqtr.time.TimeHandler.day")

    @property
    def hour(self) -> int:
        """current hour number"""
        return self._hour

    @hour.setter
    def hour(self, value: int):
        self._hour = value
        if (self._hour > MAX_DAY_HOUR):
            self._hour = MAX_DAY_HOUR
            log_warn("You have set hour > MAX_DAY_HOUR, so it will be set to MAX_DAY_HOUR.",
                     "nqtr.time.TimeHandler.hour")
        if (self._hour < MIN_DAY_HOUR):
            self._hour = MIN_DAY_HOUR
            log_warn("You have set hour < MIN_DAY_HOUR, so it will be set to MAX_DAY_HOUR.",
                     "nqtr.time.TimeHandler.hour")

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

    @property
    def weekday_number(self) -> int:
        return self.day % 7

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
        if self.hour == MAX_DAY_HOUR and amt > 0:
            log_warn("Max hour reached, you can't add more hours",
                     "nqtr.time.TimeHandler.new_hour")
            return False
        elif self.hour == MIN_DAY_HOUR and amt < 0:
            log_warn("Min hour reached, you can't remove more hours",
                     "nqtr.time.TimeHandler.new_hour")
            return False

        self.hour += amt
        return True

    def new_day(self, amt: int = 1) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day-manualy """
        if self.day == 0 and amt < 0:
            log_warn("Min day reached, you can't remove more days",
                     "nqtr.time.TimeHandler.new_day")
            return False
        self.hour = self.hour_of_new_day
        self.day += amt
        return True

    def now_is_between(self, end: int, start: int = 0, now=None) -> bool:
        if now is None:
            return (((self.hour >= start or start > end) and self.hour < end) or (self.hour >= start and (self.hour < end or start > end)))
        else:
            return (((now >= start or start > end) and now < end) or (now >= start and (now < end or start > end)))
