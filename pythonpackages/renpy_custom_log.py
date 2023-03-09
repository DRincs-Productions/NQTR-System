import renpy.exports as renpy
from pythonpackages.utility import *

__all__ = [
    "log_error",
    "log_warn",
    "log_info",
    "log_filename_line",
]

def log_error(msg: str, filename_line = None, error_notify = None):
    renpy.log("Error: " + msg)
    log_filename_line(filename_line)
    if error_notify:
        notifyExPreventsLoops(msg = error_notify)
    renpy.log("")
    return

def log_warn(msg: str, filename_line = None, warn_notify = None):
    renpy.log("Warn: " + msg)
    log_filename_line(filename_line)
    if not IsNullOrWhiteSpace(warn_notify):
        notifyExPreventsLoops(msg = warn_notify)
    renpy.log("")
    return

def log_info(msg: str, filename_line = None, info_notify = False):
    renpy.log("Info: " + msg)
    log_filename_line(filename_line)
    if not IsNullOrWhiteSpace(info_notify):
        notifyExPreventsLoops(msg = info_notify)
    renpy.log("")
    return

def log_filename_line(filename_line = None):
    if filename_line:
        renpy.log("filename_line: " + str(filename_line))
    return

