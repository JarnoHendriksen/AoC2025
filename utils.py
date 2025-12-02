
verbosity = 1

show_messages = 0b100
show_warnings = 0b010
show_errors = 0b001
hide_all = 0b000


def log_error(msg: str):
    if verbosity & show_errors:
        print("ERROR: " + msg)


def log_warning(msg: str):
    if verbosity & show_warnings:
        print("WARNING: " + msg)


def log_message(msg: str):
    if verbosity & show_messages:
        print(msg)
