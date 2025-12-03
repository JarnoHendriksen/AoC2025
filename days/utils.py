
verbosity = 1


def log_error(msg: str):
    if verbosity >= 3:
        print("ERROR: " + msg)


def log_warning(msg: str):
    if verbosity >= 2:
        print("WARNING: " + msg)


def log_message(msg: str):
    if verbosity >= 1:
        print(msg)
