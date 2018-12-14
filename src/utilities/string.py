import re

EMPTY_STRING = ''
ENDLINE = '\n'
SPACE = ' '
TAB = '\t'
UNDERSCORE = '_'


def match(pattern, s):
    return re.compile(pattern).match(s.strip()) is not None


def is_empty(s):
    return len(s.strip()) == 0


def strip_nonalphanumeric(s):
    regex = "([^\s\w]|_)+"
    return re.compile(regex).sub(EMPTY_STRING, s)


def limit_whitespace(s):
    return re.sub('[ \n\t]+', ' ', s.strip())


def format_quote(quote):
    return re.sub("[\(\[].*?[\)\]]", "", limit_whitespace(quote.replace('`', '').replace("''", '').replace(" '", "'")
                                                          .replace(" n't", "n't").strip()))


def format_character(character):
    return limit_whitespace(character).title()


def format_movie_name(name):
    return strip_nonalphanumeric(name).replace(SPACE, UNDERSCORE)


def no_whitespace(s):
    return limit_whitespace(s).replace(SPACE, EMPTY_STRING)

