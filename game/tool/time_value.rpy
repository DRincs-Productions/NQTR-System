define event_duration = 6

define hour_names = ((2, _("Night")),
            (8, _("Morning")),
            (14, _("Afternoon")),
            (20, _("Evening")),
            )
define weekday_names = (_("{#weekday}Monday"),
            _("{#weekday}Tuesday"),
            _("{#weekday}Wednesday"),
            _("{#weekday}Thursday"),
            _("{#weekday}Friday"),
            _("{#weekday}Saturday"),
            _("{#weekday}Sunday")
)
# ATTENTION here it is initialized
# when a save is loaded it is created with the updateTimeHandler() function
default tm = TimeHandler(
            hour_of_new_day = DEFAULT_HOUR_OF_NEW_DAY,
            hour = 8,
            weekend_day = 6,
            day = 0,
            event_duration = event_duration,
            hour_names = hour_names,
            weekday_names = weekday_names
)

init -8 python:
    from pythonpackages.nqtr.time import TimeHandler

    def updateTimeHandler(tm: TimeHandler) -> None:
        hour_of_new_day = DEFAULT_HOUR_OF_NEW_DAY
        hour = tm.hour
        weekend_day = tm.weekend_day
        day = tm.day_number
        tm = TimeHandler(
            hour_of_new_day=hour_of_new_day,
            hour=hour, weekend_day=weekend_day, 
            day=day,
            event_duration = event_duration,
            hour_names = hour_names,
            weekday_names = weekday_names
        )
        del hour_of_new_day
        del hour
        del weekend_day
        del day
        return