import en_core_web_sm


class NER(object):
    class __NER:
        def __init__(self):
            self.run = en_core_web_sm.load()

    instance = None

    def __new__(cls):
        if not NER.instance:
            NER.instance = NER.__NER()
        return NER.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)