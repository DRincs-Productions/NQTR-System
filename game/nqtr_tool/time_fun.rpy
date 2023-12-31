init python:
    def now_is_between(end: int, start: int = 0, now=None) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#now-is-between """
        return tm.now_is_between(end=end, start=start, now=now)

init -8 python:
    from pythonpackages.nqtr.time import TimeHandler

    def updateTimeHandler(tm: TimeHandler) -> None:
        """If you update TimeHandler settings into a new version, you can use this function to update the old save files. 
        Is used to update timeslot_names and weekday_names"""
        hour_of_new_day = tm.hour_of_new_day
        hour = tm.hour
        weekday_weekend_begins = tm.weekday_weekend_begins
        day = tm.day
        int_timeslot_names = tm.timeslot_names
        int_weekday_names = tm.timeslot_names
        if "timeslot_names" in locals() | globals():
            int_timeslot_names = timeslot_names
        if "weekday_names" in locals() | globals():
            int_weekday_names = weekday_names
        tm = TimeHandler(
            hour_of_new_day=hour_of_new_day,
            hour=hour,
            weekday_weekend_begins=weekday_weekend_begins, 
            day=day,
            timeslot_names = int_timeslot_names,
            weekday_names = int_weekday_names
        )
        del hour_of_new_day
        del hour
        del weekday_weekend_begins
        del day
        return
