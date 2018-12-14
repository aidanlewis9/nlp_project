from utilities.string import format_quote


class Character:
    def __init__(self):
        self.THRESHOLD = 5

        self.quotes = list()
        self.names = set()

    def add_names(self, names):
        name_dict = {name['n']: name['c'] for name in names}
        self.names = set(name_dict.keys())

    def add_quotes(self, quotes):
        for quote in quotes:
            self.add_quote(format_quote(quote['w']))

    def add_quote(self, quote):
        self.quotes.append(quote)

    def get_document(self):
        return " ".join(self.quotes)

    def is_necessary(self):
        return len(self.quotes) > self.THRESHOLD

    def quote_count(self):
        return len(self.quotes)
