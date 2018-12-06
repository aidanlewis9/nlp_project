import re


def match(pattern, s):
    return re.compile(pattern).match(s.strip()) is not None
