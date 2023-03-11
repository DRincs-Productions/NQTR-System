init python:
    def now_is_between(end: int, start: int = 0, now=None) -> bool:
        """Wiki: https://github.com/DRincs-Productions/NQTR-toolkit/wiki/Time-system#now-is-between """
        return tm.now_is_between(end=end, start=start, now=now)
