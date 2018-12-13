from utilities.string import limit_whitespace

import operator


class Character:
    def __init__(self, names, quotes):
        self.THRESHOLD = 5

        self.name, self.names = self.format_names(names)
        self.quotes = list()
        self.format_quotes(quotes)

    def format_names(self, names):
        name_dict = {name['n']: name['c'] for name in names}
        return max(name_dict.items(), key=operator.itemgetter(1))[0], set(name_dict.keys())

    def format_quotes(self, quotes):
        for quote in quotes:
            formatted_quote = limit_whitespace(quote['w'].replace('`', '').replace("''", '').replace(" '", "'")
                                               .replace(" n't", "n't").strip())

            self.quotes.append(formatted_quote)

    def is_relevant(self):
        return len(self.quotes) > self.THRESHOLD

    def __str__(self):
        return "Name: {}\nQuotes: {}\n".format(self.name, len(self.quotes))
