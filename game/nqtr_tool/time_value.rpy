define timeslot_names = [
    (2, _("Night")),
    (8, _("Morning")),
    (14, _("Afternoon")),
    (20, _("Evening")),
]
define weekday_names = [
    _("{#weekday}Monday"),
    _("{#weekday}Tuesday"),
    _("{#weekday}Wednesday"),
    _("{#weekday}Thursday"),
    _("{#weekday}Friday"),
    _("{#weekday}Saturday"),
    _("{#weekday}Sunday")
]
# ATTENTION here it is initialized
# when a save is loaded it is created with the updateTimeHandler() function
default tm = TimeHandler(
    hour_of_new_day = DEFAULT_HOUR_OF_NEW_DAY,
    hour = 8,
    weekday_weekend_begins = 6,
    day = 0,
    timeslot_names = timeslot_names,
    weekday_names = weekday_names
)

init -8 python:
    from pythonpackages.nqtr.time import TimeHandler

    def updateTimeHandler(tm: TimeHandler) -> None:
        """is used to update timeslot_names and weekday_names"""
        hour_of_new_day = DEFAULT_HOUR_OF_NEW_DAY
        hour = tm.hour
        weekday_weekend_begins = tm.weekday_weekend_begins
        day = tm.day
        tm = TimeHandler(
            hour_of_new_day=hour_of_new_day,
            hour=hour, weekday_weekend_begins=weekday_weekend_begins, 
            day=day,
            timeslot_names = timeslot_names,
            weekday_names = weekday_names
        )
        del hour_of_new_day
        del hour
        del weekday_weekend_begins
        del day
        return