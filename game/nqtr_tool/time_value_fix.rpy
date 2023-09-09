init -1 python:
    if not "tm" in locals() | globals():
        tm = TimeHandler(
            hour_of_new_day = 5,
            hour = 8,
            weekday_weekend_begins = 6,
            day = 0,
            timeslot_names = [],
            weekday_names = []
        )
