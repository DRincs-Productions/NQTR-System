from typing import Union
from pythonpackages.renpy_utility.renpy_custom_log import *

MIN_DAY_HOUR = 0
MAX_DAY_HOUR = 24
DEFAULT_TIME_SPENT = 1


class TimeHandler(object):
    """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#time-handler"""

    def __init__(
        self,
        hour_of_new_day: int = 5,
        hour: int = 8,
        weekday_weekend_begins: int = 6,
        day: int = 0,
        timeslot_names: list[tuple[int, str]] = [],
        weekday_names: list[str] = [],
    ):
        self.weekday_names = weekday_names
        self.hour_of_new_day = hour_of_new_day
        self.hour = hour
        self.day = day
        self.weekday_weekend_begins = weekday_weekend_begins
        self.timeslot_names = timeslot_names

    @property
    def hour_of_new_day(self) -> int:
        """hour when the day changes"""
        return self._hour_of_new_day

    @hour_of_new_day.setter
    def hour_of_new_day(self, value: int):
        self._hour_of_new_day = value
        if self._hour_of_new_day < 0:
            log_warn(
                "You have set hour_of_new_day < 0, so it will be set to 0.",
                "nqtr.time.TimeHandler.hour_of_new_day",
            )
            self._hour_of_new_day = 0

    @property
    def hour(self) -> int:
        """current hour number"""
        return self._hour

    @hour.setter
    def hour(self, value: int):
        self._hour = value
        if self._hour > MAX_DAY_HOUR:
            self._hour = MAX_DAY_HOUR
            log_warn(
                "You have set hour > MAX_DAY_HOUR, so it will be set to MAX_DAY_HOUR.",
                "nqtr.time.TimeHandler.hour",
            )
        if self._hour < MIN_DAY_HOUR:
            self._hour = MIN_DAY_HOUR
            log_warn(
                "You have set hour < MIN_DAY_HOUR, so it will be set to MAX_DAY_HOUR.",
                "nqtr.time.TimeHandler.hour",
            )

    @property
    def weekday_weekend_begins(self) -> int:
        """day when the weekend begins. this depends on the weekday_names list.
        start from 0.
        es: if weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        and weekday_weekend_begins = 6, then the weekend begins on Saturday."""
        return self._weekday_weekend_begins

    @weekday_weekend_begins.setter
    def weekday_weekend_begins(self, value: int):
        self._weekday_weekend_begins = value
        if self._weekday_weekend_begins < 0:
            log_warn(
                "You have set weekday_weekend_begins < 0, so it will be set to 6.",
                "nqtr.time.TimeHandler.weekday_weekend_begins",
            )
            self._weekday_weekend_begins = 6
        if self._weekday_weekend_begins > len(self.weekday_names):
            log_warn(
                "You have set weekday_weekend_begins > len(weekday_names), so I ignore it.",
                "nqtr.time.TimeHandler.weekday_weekend_begins",
            )

    @property
    def is_weekend(self) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-System/wiki/Time-system#is-weekend"""
        return self.weekday_number >= (self.weekday_weekend_begins - 1)

    @property
    def day(self) -> int:
        """current day number"""
        return self._day

    @day.setter
    def day(self, value: int):
        self._day = value
        if self._day < 0:
            self._day = 0
            log_warn(
                "You have set day < 0, so it will be set to 0.",
                "nqtr.time.TimeHandler.day",
            )

    @property
    def timeslot_names(self) -> list[tuple[int, str]]:
        return self._timeslot_names

    @timeslot_names.setter
    def timeslot_names(self, value: list[tuple[int, str]]):
        self._timeslot_names = value

    @property
    def weekday_names(self) -> list[str]:
        return self._weekday_names

    @weekday_names.setter
    def weekday_names(self, value: list[str]):
        self._weekday_names = value

    @property
    def timeslot_name(self) -> str:
        """Returns the name of the current timeslot."""
        if len(self.timeslot_names) > 0:
            return self.timeslot_names[self.timeslot_number][1]
        else:
            log_warn(
                "You have not set any timeslot_names, so it will return an empty string.",
                "nqtr.time.TimeHandler.timeslot_name",
            )
            return ""

    @property
    def timeslot_number(self) -> int:
        """Returns the number of the current timeslot.
        This variable is used to update images that change according to time.
        es: image = "sky-[tm.timeslot_number]"""
        res = 0
        current = None
        if len(self.timeslot_names) > 0:
            for index, timeslot in enumerate(self.timeslot_names):
                if self.hour >= timeslot[0]:
                    if current == None or timeslot[0] > current[0]:
                        res = index
                        current = timeslot
            return res
        else:
            log_error(
                "You have not set any timeslot_names, so it will return 0.",
                "nqtr.time.TimeHandler.timeslot_number",
            )
            return 0

    @property
    def weekday_number(self) -> int:
        """
        Starts from 0. Returns the number of the current weekday.
        https://github.com/DRincs-Productions/NQTR-System/wiki/Time-system#check-of-the-day-of-the-week
        """
        if len(self.weekday_names) > 0:
            return self.day % len(self.weekday_names)
        else:
            log_warn(
                "You have not set any weekday_names, so it will return 0.",
                "nqtr.time.TimeHandler.weekday_number",
            )
            return 0

    @property
    def weekday_name(self) -> str:
        if len(self.weekday_names) > 0:
            return self.weekday_names[self.weekday_number]
        else:
            log_warn(
                "You have not set any weekday_names, so it will return an empty string.",
                "nqtr.time.TimeHandler.weekday_name",
            )
            return ""

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
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-houre-manualy"""
        if self.hour == MAX_DAY_HOUR and amt > 0:
            log_info(
                "Max hour reached, you can't add more hours",
                "nqtr.time.TimeHandler.new_hour",
            )
            return False
        elif self.hour == MIN_DAY_HOUR and amt < 0:
            log_info(
                "Min hour reached, you can't remove more hours",
                "nqtr.time.TimeHandler.new_hour",
            )
            return False

        self.hour += amt
        return True

    def new_day(self, amt: int = 1) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#new-day-manualy"""
        if self.day == 0 and amt < 0:
            log_warn(
                "Min day reached, you can't remove more days",
                "nqtr.time.TimeHandler.new_day",
            )
            return False
        self.hour = self.hour_of_new_day
        self.day += amt
        return True

    def now_is_between(
        self, end: Union[int, float], start: Union[int, float] = 0, now=None
    ) -> bool:
        if now is None:
            return ((self.hour >= start or start > end) and self.hour < end) or (
                self.hour >= start and (self.hour < end or start > end)
            )
        else:
            return ((now >= start or start > end) and now < end) or (
                now >= start and (now < end or start > end)
            )
