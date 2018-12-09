import re

EMPTY_STRING = ""


def match(pattern, s):
    return re.compile(pattern).match(s.strip()) is not None


def is_empty(s):
    return len(s.strip()) == 0


def strip_nonalphanumeric(s):
    regex = "([^\s\w]|_)+"
    return re.compile(regex).sub(EMPTY_STRING, s)
