from utilities.string import match

class Parser:
    def __init__(self, title):
        self.title = title

        self.switcher = {
            "Frankenstein" : self.parse_frankenstein,
            "Jurassic Park" : self.parse_jurassic,
            "No Country for Old Men" : self.default, #self.parse_no_country,
            "Schindler's List" : self.parse_schindlers,
            "The Bourne Supremacy" : self.parse_bourne, #self.parse_bourne,
            "The Shining" : self.parse_shining,
            "The Talented Mr. Ripley" : self.parse_ripley,
            "The Wizard of Oz" : self.parse_wizard
        }

    def parse_frankenstein(self, line, scene):
        bad_string = "Free eBooks at Planet eBook.com "
        page_regex = '([0-9]{1,3}$)'
        chapter_regex = "(Chapter \d)"
        line = line.strip('\n') + ' '
        if line != bad_string and not match(page_regex, line) and not match(chapter_regex, line) and line != "Frankenstein ":
            scene.concat_sentences(line)

    def parse_jurassic(self, line, scene):
        line = line.strip('\n')
        scene.concat_sentences(line)

    def parse_schindlers(self, line, scene):
        chapter_regex = "((PROLOGUE|CHAPTER|EPILOGUE).*)"
        line = line.strip('\n') + ' '
        if not match(chapter_regex, line):
            scene.concat_sentences(line)

    def parse_bourne(self, line, scene):
        chapter_regex = "(([0-9]|[0-9][0-9])$)"
        line = line.strip('\n') + ' '
        if not match(chapter_regex, line) and line != '':
            scene.concat_sentences(line)

    def parse_shining(self, line, scene):
        chapter_regex = "(<< [0-9]* >>)"
        line = line.strip('\n') + ' '
        if not match(chapter_regex, line) and not line.isupper():
            scene.concat_sentences(line)

    def parse_ripley(self, line, scene):
        chapter_regex = "(Chapter *)"
        line = line.strip() + ' '
        if not match(chapter_regex, line):
            scene.concat_sentences(line)

    def parse_wizard(self, line, scene):
        chapter_regex = "([0-9]*\. *)"
        line = line.strip('\n') + ' '
        if not match(chapter_regex, line):
            scene.concat_sentences(line)

    def default(self, line, scene):
        line = line.strip('\n')
        scene.concat_sentences(line)

    def parse_book(self, line, scene):
        self.switcher[self.title](line, scene)
