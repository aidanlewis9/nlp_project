class Character:
    def __init__(self):
        self.THRESHOLD = 5

        self.quotes = list()
        self.names = set()

    def add_names(self, names):
        name_dict = {name['n']: name['c'] for name in names}
        self.names = set(name_dict.keys())

    def add_all_quotes(self, quotes):
        for quote in quotes:
            self.add_quote(quote)

    def add_quote(self, quote):
        self.quotes.append(quote)

    def is_relevant(self):
        return len(self.quotes) > self.THRESHOLD
