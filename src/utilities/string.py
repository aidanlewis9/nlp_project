import re

EMPTY_STRING = ''
ENDLINE = '\n'
SPACE = ' '
TAB = '\t'


def match(pattern, s):
    return re.compile(pattern).match(s.strip()) is not None


def is_empty(s):
    return len(s.strip()) == 0


def strip_nonalphanumeric(s):
    regex = "([^\s\w]|_)+"
    return re.compile(regex).sub(EMPTY_STRING, s)


def limit_whitespace(s):
    return re.sub('[ \n\t]+', ' ', s.strip())
